# Build an app that:
# Takes a sentence from user
# Sends to Gemini with instruction:
#  “Improve this sentence professionally”
# Displays improved version
# Example:
#  Input: "i want job"
#  Output: "I am seeking a professional opportunity."


from google import genai 
import os 
from dotenv import load_dotenv
import streamlit as st 

load_dotenv()
api_key = os.environ.get("GEMENI_API_KEY")
client = genai.Client(api_key=api_key)


user_prompt = st.text_input("Enter your sentence to improve:", placeholder="Type your sentence here...")

if st.button("Submit"):
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=f"Improve this sentence professionally: {user_prompt}"
    )
    st.markdown("### Gemini API Response:")
    st.markdown(response.text)