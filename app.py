import streamlit as st
from backend import (
    FIXED_DATABASES,
    load_csv_to_sqlite,
    run_query,
)

st.set_page_config(page_title="Chatbot AI - SQL Generator", page_icon="🤖", layout="wide")

st.title("🤖 Chatbot AI - Natural Language to SQL")
st.markdown("Convert natural language questions into SQL queries powered by Claude AI")

# Sidebar for database selection
st.sidebar.header("📊 Database Selection")

# Initialize session state
if "uploaded_db" not in st.session_state:
    st.session_state.uploaded_db = None
if "query_history" not in st.session_state:
    st.session_state.query_history = []

# Database options
db_options = list(FIXED_DATABASES.keys()) + ["Upload CSV"]
selected_option = st.sidebar.radio("Select a database:", db_options, index=0)

# Load database info
db_info = None
if selected_option == "Upload CSV":
    uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file:
        try:
            db_info = load_csv_to_sqlite(uploaded_file.read(), uploaded_file.name)
            st.session_state.uploaded_db = db_info
            st.sidebar.success(f"✅ Loaded: {db_info['filename']} ({db_info['row_count']} rows)")
        except Exception as e:
            st.sidebar.error(f"❌ Error loading file: {str(e)}")
else:
    db_info = FIXED_DATABASES[selected_option]
    st.session_state.uploaded_db = None

# Main content area
if db_info:
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📝 Ask a Question")
        question = st.text_area(
            "Enter your question in natural language:",
            placeholder="e.g., 'Show me the top 10 most expensive products'",
            height=100
        )
    
    with col2:
        st.subheader("📋 Database Info")
        st.write(f"**Tables:** {len(db_info['tables'])}")
        for table_name in db_info['tables']:
            st.write(f"- {table_name}")
    
    # Execute query
    if st.button("🚀 Execute Query", use_container_width=True):
        if not question.strip():
            st.warning("⚠️ Please enter a question")
        else:
            with st.spinner("⏳ Generating and executing SQL..."):
                try:
                    result = run_query(
                        question,
                        db_info['tables'],
                        db_info['path'],
                        desc=selected_option
                    )
                    
                    # Add to history
                    st.session_state.query_history.append({
                        "question": question,
                        "sql": result["sql_query"],
                        "rows": result["row_count"]
                    })
                    
                    st.success(f"✅ Query executed successfully ({result['row_count']} rows)")
                    
                    # Display SQL
                    st.subheader("🔍 Generated SQL")
                    st.code(result["sql_query"], language="sql")
                    
                    # Display results
                    st.subheader("📊 Results")
                    if result["rows"]:
                        st.dataframe(
                            result["rows"],
                            column_config={col: col for col in result["columns"]},
                            use_container_width=True,
                            height=400
                        )
                        
                        # Download button
                        import pandas as pd
                        df = pd.DataFrame(result["rows"], columns=result["columns"])
                        csv = df.to_csv(index=False)
                        st.download_button(
                            label="📥 Download CSV",
                            data=csv,
                            file_name="query_results.csv",
                            mime="text/csv"
                        )
                    else:
                        st.info("No results found")
                
                except ValueError as e:
                    st.error(f"❌ Error: {str(e)}")
                except Exception as e:
                    st.error(f"❌ Unexpected error: {str(e)}")
    
    # Query history
    if st.session_state.query_history:
        st.sidebar.subheader("📜 Query History")
        for i, query in enumerate(reversed(st.session_state.query_history[-5:]), 1):
            with st.sidebar.expander(f"Query {i}: {query['question'][:30]}..."):
                st.code(query['sql'], language="sql")
                st.caption(f"Rows: {query['rows']}")

else:
    st.warning("⚠️ Please select or upload a database to get started")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center'>
        <p>Built with ❤️ using Streamlit + Claude AI</p>
        <p><a href='https://github.com/victorcarvalh09/chatbot_ai'>View on GitHub</a></p>
    </div>
    """,
    unsafe_allow_html=True
)
