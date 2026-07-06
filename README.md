# Chatbot AI - Natural Language to SQL (OpenAI Edition)

A Streamlit application that converts natural language questions into SQL queries using OpenAI's GPT models.

## Features

- 🤖 AI-powered SQL generation using GPT-4o-mini
- 🔒 Built-in security (forbidden SQL commands detection)
- 📊 Support for multiple databases
- 📁 CSV file upload and automatic SQLite conversion
- 💾 Query execution and result display

## Requirements

- Python 3.8+
- OpenAI API Key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/victorcarvalh09/chatbot_ai.git
cd chatbot_ai
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create `.streamlit/secrets.toml`:
```toml
OPENAI_API_KEY = "your-api-key-here"
```

4. Run locally:
```bash
streamlit run app.py
```

## Deployment on Streamlit Cloud

### Step 1: Push to GitHub
Your code is already on GitHub. Make sure all files are committed.

### Step 2: Deploy on Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click **"New app"**
3. Select:
   - Repository: `victorcarvalh09/chatbot_ai`
   - Branch: `main`
   - Main file path: `app.py`
4. Click **"Deploy"**

### Step 3: Add Secrets
1. After deployment, click **"Advanced settings"** → **"Secrets"**
2. Add your OpenAI API key:
```toml
OPENAI_API_KEY = "sk-proj-your-api-key-here"
```

## Usage

1. Select a database or upload a CSV file
2. Type your question in natural language
3. The app generates and executes SQL using GPT-4o-mini
4. Results are displayed in a table

## Security

- ✅ Only SELECT queries allowed
- ✅ Forbidden SQL operations blocked (INSERT, UPDATE, DELETE, DROP, etc.)
- ✅ Query validation before execution
- ✅ Column name escaping for special characters

## Model

- **Model**: `gpt-4o-mini` (cost-effective and reliable)
- **Alternative**: Change `MODEL_ID` in `backend.py` to use other models like `gpt-4` or `gpt-3.5-turbo`

## License

MIT

## Author

victorcarvalh09
