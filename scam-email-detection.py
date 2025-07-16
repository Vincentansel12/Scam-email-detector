import streamlit as st
from openai import OpenAI

# Setup OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="🕵️ Scam Email Detector", layout="centered")
st.title("🕵️ Scam Email Detector")

st.markdown("Paste your email below:")

# Text input
email_text = st.text_area(" ", height=250)

if st.button("Check if Scam"):
    if email_text.strip():
        # Enhanced Prompt
        prompt = f"""
You are a scam email detection expert.

Carefully analyze the email below and determine if it is a scam or not. 

Use multiple signals in combination — do **not** flag an email as a scam just because it contains a shortened URL.

Instead, consider these factors:
- Does it create urgency (e.g., tight deadlines, “must act now”)?
- Does it ask for personal information (name, ID, bank details, CV)?
- Is the sender's identity or email domain unverifiable or suspicious?
- Is there a shortened URL **combined** with a request to click or submit data?
- Is the language generic, overly formal, or lacking clear contact details?
- Does the email mimic a legitimate brand but fail to use official domain names?

Make your judgment in **one sentence**, starting with one of:
- "Yes, this is a scam because ..."
- "No, this is not a scam because ..."
- "It is unclear if this is a scam because ..."

Be especially careful with emails requesting data submission via shortened links, or that appear to impersonate well-known companies.

Here is the email:
{email_text}
"""

        # Call OpenAI
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )

        reply = response.choices[0].message.content.strip()

        # Display result with coloring
        if reply.lower().startswith("yes"):
            st.error(f"🔴 Result: {reply}")
        elif reply.lower().startswith("no"):
            st.success(f"🟢 Result: {reply}")
        elif reply.lower().startswith("it is unclear"):
            st.warning(f"🟡 Result: {reply}")
        else:
            st.info(f"🟣 Result: {reply}")
    else:
        st.warning("Please enter an email.")
