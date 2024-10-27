import streamlit as st
from langchain_openai import OpenAI

st.title("Chat via Langchain OpenAI")

llm = OpenAI(model="gpt-3.5-turbo", temperature=0.5, api_key=st.secrets["OpenAI_key"])

with st.form("chatform"):
    prompt = st.text_area(label = "Enter text:", 
                        value = "how to use langchain?",
                        placeholder="type your question here")
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.info(llm.invoke(prompt))
