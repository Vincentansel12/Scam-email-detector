import streamlit as st
from openai import OpenAI

# Set up Streamlit UI
st.set_page_config(page_title="Scam Email Detector", page_icon="🕵️‍♂️")
st.title("🕵️‍♂️ Scam Email Detector")
st.write("Paste your email below:")

# Text input
email_text = st.text_area("", height=300)
submit = st.button("Check if Scam")

# Prompt logic
prompt_template = f"""
You are an expert in scam email detection.

Your task is to analyze the email content below and determine whether it is a scam or not.

Please follow these steps in your reasoning:

1. Ignore any repeated legal disclaimers or email footer signatures.
2. Focus on signs of psychological pressure or urgency (e.g., "immediately", "or else", "final warning").
3. Identify requests for personal credentials or sensitive actions (e.g., filling forms, uploading data, making payments).
4. Examine the use of shortened URLs (e.g., bit.ly, tinyurl), but consider their context. For example, Zoom or attendance links from known institutions may be legitimate.
5. Assess the sender's language, grammar, professionalism, and whether it aligns with typical scam patterns.
6. Consider if the content sounds credible coming from a professional organization or institution.

Finally, write a **clear and concise one-sentence judgment** using one of the following formats:

- "Yes, this is a scam because ..."
- "No, this is not a scam because ..."
- "It is unclear if this is a scam because ..."

Email content to analyze:
\"\"\"{email_text}\"\"\"
"""

# Handle submission
if submit and email_text.strip() != "":
    with st.spinner("Analyzing..."):
        try:
            client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

            response = client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt_template}],
                temperature=0
            )

            output = response.choices[0].message.content.strip()

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
