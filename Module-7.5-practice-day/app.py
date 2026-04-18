import streamlit as st
from api import code_debugger
from PIL import Image

st.title("AI Code Debugger")
st.markdown("Upload your code file to get it debugged by AI.")
st.divider()

with st.sidebar:
    st.header("Upload your code snippet")
    images = st.file_uploader("Add your code screenshot here", type=["jpg", "jpeg", "png"], accept_multiple_files=True)
    images = [Image.open(image) for image in images]  # Open each uploaded image using PIL
    if images:
        if len(images) > 3:
            st.warning("Please upload a maximum of 3 images.")
        else:
            st.success(f"{len(images)} image(s) uploaded successfully!")
            st.subheader("Uploaded Images:")
            col = st.columns(len(images))
            for i, img in enumerate(images): # enumerate to get index and image
                col[i].image(img, caption=f"Image {i+1}")
    # Option bar
    st.header("Select an option")
    option = st.selectbox("Choose an option", options=["Debug Code", "Explain Code", "Optimize Code"], key="option_selection", index=None)
    if option:
        st.markdown(f"You have selected **{option}** option.")
    else:
        st.warning("Please select an option to proceed.")
    
    pressed_btn = st.button("Submit", key="submit_button", type="primary")

if pressed_btn:
    if not images:
        st.error("Please upload at least one image to proceed.")
    elif not option:
        st.error("Please select an option to proceed.")
    else:
        st.success(f"Processing your request for **{option}**...")
        # Here you can add the logic to process the images and perform the selected action (debug, explain, optimize) based on the uploaded code snippet.

        with st.container(border=True):
            st.subheader(f"{option} Result")
            st.text(f"This is where the AI-generated {option.lower()} result will be displayed.")
            with st.spinner(f"Generating {option.lower()} result..."):
                # Generate the result based on the selected option and uploaded images
                result = code_debugger(images, option)  # Call the code_debugger function with the uploaded images and selected option
                st.markdown(f"### Gemini API Response:\n{result}")  # Display the generated result

                st.balloons()