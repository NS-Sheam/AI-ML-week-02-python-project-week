# Create an app that:
# Takes a prompt from user
# Sends it to Gemini API
# Displays the generated response

from google import genai 
import os 
from dotenv import load_dotenv
import streamlit as st 

load_dotenv()
api_key = os.environ.get("GEMENI_API_KEY")
client = genai.Client(api_key=api_key)

user_prompt = st.text_input("Enter your prompt for Gemini API:", placeholder="Type your prompt here...")

if st.button("Submit"):
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=user_prompt
    )
    st.markdown("### Gemini API Response:")
    st.markdown(response.text)