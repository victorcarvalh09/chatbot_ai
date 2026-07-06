# Chatbot AI Deployment Guide - OpenAI Edition

## ✅ Deployment Ready!

Your repository is now configured to use **OpenAI's GPT-4o-mini** model for SQL generation.

### 📁 Files Updated:
- ✅ `backend.py` - Updated to use OpenAI API
- ✅ `requirements.txt` - Updated with OpenAI library
- ✅ `README.md` - Updated documentation
- ✅ `app.py` - Streamlit frontend (ready to use)
- ✅ `.streamlit/config.toml` - Streamlit configuration

---

## 🚀 Deploy to Streamlit Cloud

### Step 1: Go to Streamlit Cloud
Visit **[share.streamlit.io](https://share.streamlit.io)** and sign in with GitHub

### Step 2: Create New App
1. Click **"New app"**
2. Select your repository: `victorcarvalh09/chatbot_ai`
3. Select branch: `main`
4. Set main file path: `app.py`
5. Click **"Deploy"**

### Step 3: Add OpenAI API Key (IMPORTANT!)
Once deployed:
1. Click the **⋮** menu (top right)
2. Select **"Settings"**
3. Go to **"Secrets"** tab
4. Add your OpenAI API key:

```toml
OPENAI_API_KEY = "sk-proj-xxxxxxxxxxxxx"
```

Save and the app will restart with your API key.

---

## 🔑 How to Get Your OpenAI API Key

1. Go to **[platform.openai.com](https://platform.openai.com)**
2. Sign in or create an account
3. Navigate to **"API Keys"** in your account settings
4. Click **"Create new secret key"**
5. Copy the key and paste it in Streamlit Cloud secrets

**Important**: Keep your API key secure and never share it!

---

## 💰 Costs

- **gpt-4o-mini** is the most cost-effective model for SQL generation
- Typical usage costs a few cents per 1000 queries
- You can monitor usage in your OpenAI dashboard

---

## 📊 Local Testing (Optional)

To test locally before deploying:

```bash
# Install dependencies
pip install -r requirements.txt

# Create secrets file
mkdir -p .streamlit
echo 'OPENAI_API_KEY = "your-key-here"' > .streamlit/secrets.toml

# Run the app
streamlit run app.py
```

---

## 🛡️ Security Features

- ✅ Only SELECT queries allowed
- ✅ Forbidden SQL operations blocked
- ✅ Query validation before execution
- ✅ API key stored securely in Streamlit Cloud
- ✅ Column name escaping for special characters

---

## 📝 Usage

1. **Select Database**: Choose from predefined databases or upload a CSV
2. **Ask Question**: Enter a natural language question
3. **View Results**: See generated SQL and query results
4. **Download Data**: Export results as CSV

---

## 🔧 Customization

### Change AI Model
Edit `backend.py` line 8 to use a different model:

```python
MODEL_ID = "gpt-4o-mini"  # Change this to:
# MODEL_ID = "gpt-4"  # More powerful, costs more
# MODEL_ID = "gpt-3.5-turbo"  # Faster, less expensive
```

---

## 🆘 Troubleshooting

| Issue | Solution |
|-------|----------|
| "OPENAI_API_KEY not found" | Add your API key to Streamlit Cloud Secrets |
| "Invalid API key" | Check that your key is correct and not expired |
| App won't load | Check that `requirements.txt` has all dependencies |
| Query fails | Ensure your natural language question is clear |
| High costs | Use `gpt-3.5-turbo` instead for lower costs |

---

## 📞 Support

- **OpenAI Documentation**: [platform.openai.com/docs](https://platform.openai.com/docs)
- **Streamlit Docs**: [docs.streamlit.io](https://docs.streamlit.io)
- **GitHub Issues**: [Open an issue](https://github.com/victorcarvalh09/chatbot_ai/issues)

---

**Your app is ready to deploy! 🎉**

Visit [share.streamlit.io](https://share.streamlit.io) to get started.
