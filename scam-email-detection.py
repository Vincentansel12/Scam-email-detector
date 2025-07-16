import openai
import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Streamlit UI
st.set_page_config(page_title="Scam Email Detector", page_icon="🕵️‍♂️")
st.title("🕵️‍♂️ Scam Email Detector")
st.write("Paste your email below:")

email_text = st.text_area("", height=300)
submit = st.button("Check if Scam")

# Prompt template with reasoning steps
prompt_template = f"""
You are a scam email detection expert.

Analyze the email below carefully and determine if it's a scam or not.

Follow this process:
1. Check if there is urgency or pressure.
2. Check if there is a request for personal data or links to unknown websites.
3. Check if the sender domain is verifiable or suspicious.
4. Check if any shortened URLs are used with unclear purpose.
5. Consider if the message aligns with typical scam patterns.

Then summarize your conclusion in **one sentence** that starts with one of the following:
- "Yes, this is a scam because ..."
- "No, this is not a scam because ..."
- "It is unclear if this is a scam because ..."

Here is the email:
\"\"\"{email_text}\"\"\"
"""

if submit and email_text.strip() != "":
    with st.spinner("Analyzing..."):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt_template}],
                temperature=0
            )

            output = response['choices'][0]['message']['content'].strip()

            if output.lower().startswith("yes, this is a scam"):
                st.error(f"🔴 Result: {output}")
            elif output.lower().startswith("no, this is not a scam"):
                st.success(f"🟢 Result: {output}")
            else:
                st.warning(f"🟡 Result: {output}")
        except Exception as e:
            st.error(f"Error: {str(e)}")

elif submit:
    st.warning("Please enter an email for analysis.")
