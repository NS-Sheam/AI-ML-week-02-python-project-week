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

    # if selected_option:
    #     st.markdown(f"You have selected **{selected_option}** difficulty level.")
    # else:
    #     st.warning("Please select a difficulty level.")

    pressed = st.button("Generate Note Summery and Quiz", key="generate_button", type="primary")


if pressed:
    if not images:
        st.error("Please upload at least one image to generate note summery and quiz.")
    elif not selected_option:
        st.error("Please select a difficulty level to generate note summery and quiz.")
    else:
        st.success("Generating note summery and quiz...")
        # Here you can add the logic to process the images and generate the note summery and quiz based on the selected difficulty level.
        # Note

        with st.container(border=True):
            st.subheader("Note Summery")
            st.text("This is where the generated note summery will be displayed.")

        # Audio transcription

        with st.container(border=True):
            st.subheader("Audio Transcription")
            st.text("This is where the generated audio transcription will be displayed.")

        # Quiz generation
        with st.container(border=True):
            st.subheader(f"Quiz ({selected_option} Difficulty)")
            st.text("This is where the generated quiz will be displayed.")