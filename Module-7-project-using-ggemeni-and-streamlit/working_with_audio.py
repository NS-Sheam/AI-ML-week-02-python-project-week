from gtts import gTTS
import io
import streamlit as st

text = "Hello, this is a text-to-speech conversion using gTTS in Python."

speech = gTTS(text=text, lang='en', slow=False)

# Save the audio to a BytesIO object
audio_buffer = io.BytesIO()
speech.write_to_fp(audio_buffer)

st.audio(audio_buffer, format="audio/mp3")