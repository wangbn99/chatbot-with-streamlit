import streamlit as st
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate

st.title("Roadmap for Learning a Specific Topic")

with st.form("stform"):
    topic = st.text_input("Enter prompt:", "")
    submitted = st.form_submit_button("Submit")
    if submitted:
        llm = OpenAI(model="gpt-3.5-turbo", api_key=st.secrets["OpenAI_key"])
        template = "As an expert, please provide a roadmap for learning {topic}."
        prompt_template = PromptTemplate.from_template(template=template)
        formated_prompt_template = prompt_template.format(topic=topic)
        response = llm.invoke(formated_prompt_template)
        st.info(response)
