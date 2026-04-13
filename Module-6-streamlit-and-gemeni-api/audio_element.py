import streamlit as st 

st.title("Input your files (audio)",anchor=False)
st.divider()

#from directory
# st.audio("audio/welcome.mp3",loop=True)

st.divider()


audio_file = st.file_uploader("Enter your audio",
                 type=['mp3','ogg','flac'],
                 accept_multiple_files= True,
                 )



print(type(audio_file))

if audio_file:
    for per_audio in audio_file:
        st.audio(per_audio)
