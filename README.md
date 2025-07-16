# 🕵️ Scam Email Detector

This is a simple yet powerful web app built with **Streamlit** and **OpenAI GPT-4** to detect whether an email is potentially a scam.

---

## ✨ Features

- ✅ Paste any email content and get a quick analysis
- 🤖 Uses GPT-4 to classify if the email is a scam
- 🟢 Displays a clear result (Scam or Not) with a short reasoning
- 🎨 Clean and responsive UI with Streamlit

---

## 📦 Tech Stack

- Python 3.10+
- Streamlit
- OpenAI GPT-4 API
- dotenv (.env) for API key management

---

## 🚀 Getting Started

### 1. Clone the repo

git clone https://github.com/Vincentansel12/scam-email-detector.git
cd scam-email-detector 

### 2. Install dependencies

pip install -r requirements.txt

### 3. Set your OpenAI API Key

Create a .env file in the root directory:

OPENAI_API_KEY=your_openai_api_key_here

### 4. Run the app

streamlit run app.py

🧠 How It Works

This app sends the email content to GPT-4 with a custom prompt like:

"Is the following email a scam? Answer only with Yes or No in a full sentence. Then, explain your reasoning."
It then displays:

The AI's decision (with color indicator)
A brief reasoning of the judgment
<img width="616" height="381" alt="image" src="https://github.com/user-attachments/assets/019f39d2-3b29-485a-a13e-8b3f249d64b9" />

<img width="591" height="447" alt="image" src="https://github.com/user-attachments/assets/5b620a44-4393-4b73-aafa-7705884967ec" />


🧪 Example Emails

Legit Email: Welcome email from a product or platform
Scam Email: Message asking for urgent data input via shortlink (e.g., bit.ly)
📌 Disclaimer

This tool provides AI-based support for scam detection but is not a replacement for human judgment. Always verify suspicious emails independently.

🧑‍💻 Author

Vincentius Ansel Suppa
Data Science Master's Student @ University of Sydney
GitHub: Vincentansel12
LinkedIn: linkedin.com/in/vincentiusansel/
