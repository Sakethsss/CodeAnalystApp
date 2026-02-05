# 🧠 Python Code Analyst App

A **Streamlit-based AI code review application** powered by **Google Gemini**.  
Upload any Python (`.py`) file and get an instant, detailed code review covering best practices, bugs, performance, security, and structure.

---

## 🚀 Features

- Upload and preview Python source code
- AI-powered code review using **Google Gemini**
- Suggestions for:
  - Code quality & PEP 8 best practices
  - Bug detection & edge cases
  - Performance optimization
  - Security concerns
  - Code structure & modularity
- Clean and interactive Streamlit UI

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **Google Generative AI (Gemini)**
- **python-dotenv**

---

## 📦 Installation & Setup

### 1️⃣ Clone the repository

git clone https://github.com/your-username/code-analyst-app.git
cd code-analyst-app
2️⃣ Create a virtual environment (recommended)
python -m venv venv
Activate it:

Windows

venv\Scripts\activate
Mac / Linux

source venv/bin/activate
3️⃣ Install dependencies
pip install -r requirements.txt
If you don’t have a requirements.txt, install manually:

pip install streamlit python-dotenv google-generativeai
🔑 Gemini API Key Setup
1️⃣ Create a Gemini API Key
Visit 👉 https://aistudio.google.com/

Sign in with your Google account

Go to API Keys

Click Create API Key

Copy the generated key

2️⃣ Create a .env file
In the project root directory, create a file named .env and add:

GEMINI_API_KEY=your_gemini_api_key_here
⚠️ Do NOT commit your .env file
Make sure it’s included in .gitignore.

▶️ Running the App
streamlit run app.py
(Replace app.py with your main file name if different.)

The app will open automatically in your browser.

