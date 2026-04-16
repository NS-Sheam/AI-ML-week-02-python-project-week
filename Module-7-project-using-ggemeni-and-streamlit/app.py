import streamlit as st

# Title and description
st.title("Note summery and quiz generator")
st.markdown("Upload upto 3 images to generate note summery and quiz")
st.divider()

with st.sidebar:

    # image upload section
    st.header("Upload your images")
    images = uploaded_files = st.file_uploader("Choose images", accept_multiple_files=True, type=["jpg", "jpeg", "png"])

    if images:
        if len(images) > 3:
            st.warning("Please upload a maximum of 3 images.")
        else:
            st.success(f"{len(images)} image(s) uploaded successfully!")
            st.subheader("Uploaded Images:")
            col = st.columns(len(images))
            for i, img in enumerate(images): # enumerate to get index and image
                col[i].image(img, caption=f"Image {i+1}") 

    # difficulty level selection
    st.header("Select difficulty level")
    selected_option = st.selectbox("Difficulty Level", options=["Easy", "Medium", "Hard"], key="difficulty", index = None)

    if selected_option:
        st.markdown(f"You have selected **{selected_option}** difficulty level.")
    else:
        st.warning("Please select a difficulty level.")

    st.button("Generate Note Summery and Quiz", key="generate_button", type="primary")
