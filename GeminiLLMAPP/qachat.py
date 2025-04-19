from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load Gemini pro model and get repsonse from

model=genai.GenerativeModel("gemini-2.0-flash")
chat=model.start_chat(history=[])

def get_gimini_response(question):
    respsonse=chat.send_message(question,stream=True)
    return respsonse

## initialize our streamlit app

st.set_page_config(page_title="Q&A Demo")
st.header("MY ChatBot")

## Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []
    
input=st.text_input("Input: " ,key="input")
submit=st.button("Ask the Question")

if submit and input:
    response=get_gimini_response(input)
## Add user query and response to session chat history
    st.session_state['chat_history'].append(("You", input))
    st.subheader("The Response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot",chunk.text))
st.subheader("The Chat history is")

for role,text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")