import streamlit as st

st.title("Media Element Example", anchor=False, width=400)
st.divider()

image = st.file_uploader("Upload a file", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

print(type(image))

if image:
    col  = st.columns(len(image))
    for i, per_image in enumerate(image):
        with col[i]:
            st.image(per_image, caption=per_image.name)