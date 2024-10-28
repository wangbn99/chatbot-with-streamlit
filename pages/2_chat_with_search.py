import streamlit as st

from langchain.agents import initialize_agent, AgentType
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.callbacks import StreamlitCallbackHandler
from langchain_openai import ChatOpenAI

st.title("Chat with DDG Search")

llm = ChatOpenAI(model="gpt-3.5-turbo", api_key=st.secrets["OpenAI_key"], streaming=True)

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hi, what can I help with?"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])
  
if prompt := st.chat_input(placeholder="message LangChain search tool"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    search = DuckDuckGoSearchRun()
    agent = initialize_agent(
        [search], llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, handle_parsing_errors=True
    )
    with st.chat_message("assistant"):
        st_handler = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
        response = agent.run(st.session_state.messages, callbacks=[st_handler])
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.write(response)
