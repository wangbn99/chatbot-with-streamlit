import streamlit as st
from openai import OpenAI
from openai import AuthenticationError

st.title("Chatbot with OpenAI")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "What can I help with?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])


client = OpenAI(api_key=st.secrets["OpenAI_key"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    try:
        response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
        msg = response.choices[0].message.content
    except AuthenticationError as e:
        msg = e.message
    except Exception as e:
        msg = e.message
    else:
        msg = "Error response from GPT"       
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
