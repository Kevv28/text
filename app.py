import streamlit as st
from summarizer import summarize_text

st.set_page_config(page_title="AI Text Summarizer", layout="centered")

st.title(" AI-Powered Text Summarizer")
st.write("Paste any article, blog, or text below and get a **3-sentence summary** using Groq API.")

# User Input
user_text = st.text_area("Enter text to summarize:", height=250)

if st.button("Summarize"):
    if user_text.strip():
        with st.spinner("Summarizing..."):
            summary = summarize_text(user_text)
        st.subheader("Summary:")
        st.success(summary)
    else:
        st.warning(" Please enter some text first.")
