import streamlit as st
import language_tool_python

# Initialize grammar tool
tool = language_tool_python.LanguageTool('en-US')

st.set_page_config(page_title="AI Grammar Checker", layout="centered")

st.title("✍️ AI Grammar Checker (Offline)")
st.write("Fix grammar and improve sentence clarity — no API key required.")

# Input text
text = st.text_area(
    "Enter your text:",
    height=200,
    placeholder="Type or paste your text here..."
)

if st.button("✅ Check Grammar"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        with st.spinner("Checking grammar..."):
            matches = tool.check(text)
            corrected_text = language_tool_python.utils.correct(text, matches)

        st.success("Grammar corrected!")
        st.text_area("Corrected Text:", corrected_text, height=200)
