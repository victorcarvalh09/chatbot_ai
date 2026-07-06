import re
import sqlite3
import tempfile
import pandas as pd
import streamlit as st
from openai import OpenAI

MODEL_ID = "gpt-4o-mini"

FIXED_DATABASES = {
    "database_example": {
        "path": "database_example.db",
        "tables": {
            "produtos": [{"name": "id", "type": "INTEGER"}, {"name": "nome", "type": "TEXT"}, {"name": "preco", "type": "REAL"}],
            "vendas": [{"name": "id", "type": "INTEGER"}, {"name": "produto_id", "type": "INTEGER"}, {"name": "quantidade", "type": "INTEGER"}, {"name": "data_venda", "type": "TEXT"}],
        },
    },
    "central_database": {
        "path": "central_database.db",
        "tables": {
            "searched_with_rising_searches_BR_20260601_1141_20260608_1141": [
                {"name": "query", "type": "TEXT"}, {"name": "search interest", "type": "INTEGER"}, {"name": "increase percent", "type": "TEXT"}
            ]
        },
    },
}

FORBIDDEN = re.compile(r"\b(INSERT|UPDATE|DELETE|DROP|CREATE|ALTER|TRUNCATE|ATTACH|DETACH|PRAGMA|EXEC)\b", re.IGNORECASE)
SQL_TAG = re.compile(r"<sql>(.*?)</sql>", re.DOTALL | re.IGNORECASE)


def get_client():
    # Lê a chave dos secrets do Streamlit Cloud
    return OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


def _schema_block(tables):
    lines = []
    for t, cols in tables.items():
        col_defs = ", ".join(f"{c['name']} {c['type']}" for c in cols)
        lines.append(f"  - {t} ({col_defs})")
    return "\n".join(lines)


def build_system_prompt(tables, desc=""):
    return f"""Você é um especialista em SQL para SQLite. Converta perguntas em linguagem natural em SQL.
{f'Contexto: {desc}' if desc else ''}

ESQUEMA:
{_schema_block(tables)}

REGRAS:
1. Retorne APENAS a query entre <sql> e </sql>.
2. SOMENTE SELECT. Nunca INSERT/UPDATE/DELETE/DROP/DDL.
3. Use nomes de tabelas/colunas exatamente como no esquema.
4. Colunas com espaços entre aspas duplas (ex: "search interest").
5. Use LIMIT 1000 quando não houver filtro.

Exemplo: <sql>SELECT nome, preco FROM produtos ORDER BY preco DESC LIMIT 10</sql>"""


def extract_sql(response):
    m = SQL_TAG.search(response)
    if not m:
        raise ValueError("O modelo não retornou SQL válido.")
    sql = m.group(1).strip()
    if FORBIDDEN.search(sql):
        raise ValueError("Query rejeitada por segurança (operação não permitida).")
    if not sql.upper().lstrip().startswith("SELECT"):
        raise ValueError("Apenas SELECT é permitido.")
    return sql


def load_csv_to_sqlite(file_bytes, filename):
    df = pd.read_csv(pd.io.common.BytesIO(file_bytes), low_memory=False, encoding_errors="replace")
    table = "csv_" + re.sub(r"[^a-z0-9_]", "_", filename.lower().replace(".csv", ""))
    tmp = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
    db_path = tmp.name
    tmp.close()
    conn = sqlite3.connect(db_path)
    df.to_sql(table, conn, if_exists="replace", index=False)
    conn.close()
    tmap = {"int64": "INTEGER", "float64": "REAL", "bool": "INTEGER", "object": "TEXT"}
    columns = [{"name": c, "type": tmap.get(str(dt), "TEXT")} for c, dt in df.dtypes.items()]
    return {"db_path": db_path, "table_name": table, "columns": columns, "row_count": len(df), "filename": filename, "tables": {table: columns}}


def run_query(question, tables, db_path, desc=""):
    client = get_client()
    system = build_system_prompt(tables, desc)
    msg = client.chat.completions.create(
        model=MODEL_ID,
        max_tokens=1024,
        system=system,
        messages=[{"role": "user", "content": question}]
    )
    sql = extract_sql(msg.choices[0].message.content)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(sql)
    rows_raw = cur.fetchall()
    columns = [d[0] for d in cur.description] if cur.description else []
    rows = [list(r) for r in rows_raw]
    conn.close()
    return {"sql_query": sql, "columns": columns, "rows": rows, "row_count": len(rows)}
