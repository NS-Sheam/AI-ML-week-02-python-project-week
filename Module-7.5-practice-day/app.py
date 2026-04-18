import streamlit as st

st.title("AI Code Debugger")
st.markdown("Upload your code file to get it debugged by AI.")
st.divider()

with st.sidebar:
    st.header("Upload your code snippet")
    images = st.file_uploader("Add your code screenshot here", type=["jpg", "jpeg", "png"], accept_multiple_files=True)
    if images:
        if len(images) > 3:
            st.warning("Please upload a maximum of 3 images.")
        else:
            st.success(f"{len(images)} image(s) uploaded successfully!")
            st.subheader("Uploaded Images:")
            col = st.columns(len(images))
            for i, img in enumerate(images): # enumerate to get index and image
                col[i].image(img, caption=f"Image {i+1}")