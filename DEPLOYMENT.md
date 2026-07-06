# Chatbot AI Deployment Guide

## ✅ Deployment Completed!

Your repository is now ready for deployment on **Streamlit Cloud**.

### 📁 Files Created:
- ✅ `app.py` - Main Streamlit application
- ✅ `backend.py` - Business logic and SQL generation
- ✅ `requirements.txt` - Python dependencies
- ✅ `.streamlit/config.toml` - Streamlit configuration
- ✅ `README.md` - Documentation
- ✅ `.gitignore` - Git ignore rules

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

### Step 3: Add API Key (IMPORTANT!)
Once deployed:
1. Click the **⋮** menu (top right)
2. Select **"Settings"**
3. Go to **"Secrets"** tab
4. Add your Anthropic API key:

```toml
ANTHROPIC_API_KEY = "sk-ant-xxxxxxxxxxxxx"
```

Save and the app will restart with your API key.

---

## 🔑 How to Get Your Anthropic API Key

1. Go to **[console.anthropic.com](https://console.anthropic.com)**
2. Sign in or create an account
3. Navigate to **"API Keys"**
4. Click **"Create Key"**
5. Copy the key and paste it in Streamlit Cloud secrets

---

## 📊 Local Testing (Optional)

To test locally before deploying:

```bash
# Install dependencies
pip install -r requirements.txt

# Create secrets file
mkdir -p .streamlit
echo 'ANTHROPIC_API_KEY = "your-key-here"' > .streamlit/secrets.toml

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

## 🆘 Troubleshooting

| Issue | Solution |
|-------|----------|
| "ANTHROPIC_API_KEY not found" | Add your API key to Streamlit Cloud Secrets |
| App won't load | Check that `requirements.txt` has all dependencies |
| Query fails | Ensure your natural language question is clear and specific |
| Database not found | Make sure database files exist or upload a CSV |

---

## 📞 Support

- **Streamlit Docs**: [docs.streamlit.io](https://docs.streamlit.io)
- **Anthropic API Docs**: [docs.anthropic.com](https://docs.anthropic.com)
- **GitHub Issues**: [Open an issue](https://github.com/victorcarvalh09/chatbot_ai/issues)

---

**Your app is ready to deploy! 🎉**
