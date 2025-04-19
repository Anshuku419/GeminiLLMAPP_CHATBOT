from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load Gemini pro model and get repsonse from
model=genai.GenerativeModel("gemini-2.0-flash")
def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text

## initialize our stramlit app

st.set_page_config(page_title="Q&A Demo")

st.header("MY ChatBot")

input=st.text_input("Input: " ,key="input")
submit=st.button("Ask the question")
## When submit is clicked
if submit:
    response=get_gemini_response(input)
    st.write(response)