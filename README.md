# 🎈 Chatbot With Streamlit

This app demostrats how to use Streamlit to create a chatbot UI and interacts with OpenAI API and LangChain API. 

## Requiremnets
To correctly run the app, an OpenAI API key is needed to set in secrets.toml configuration fileas below:
```sh
.\.streamlit\secrets.toml
OpenAI_key='xxxxxxxxxxxx'
```
You can go to https://platform.openai.com/account/api-keys get your OpenAI API key

## Run locally

```sh
python -m venv .venv
.venv/Scripts/activate
pip install -r requirements.txt
streamlit run Chatbot.py
```
