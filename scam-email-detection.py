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

Analyze the email below carefully and determine if it's a scam or not.

Give your judgment in one sentence **starting with**:
- "Yes, this is a scam because ..." OR
- "No, this is not a scam because ..." OR
- "It is unclear if this is a scam because ..."

Be especially cautious of shortened URLs (like bit.ly), urgent deadlines, requests to click links, or any attempt to collect personal data.

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
