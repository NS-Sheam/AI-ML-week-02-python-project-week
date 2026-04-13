import streamlit as st

st.title("Text Input Example", anchor=False, width=400)
st.header("Welcome to the Text Input Example!", divider=True)
st.subheader("Enter some text below:")
st.text("You can use this text input to enter any information you'd like. It's a great way to collect user input in your Streamlit app.")
user_input = st.text_input("Your input:")
st.write("This is a text input example.")

st.markdown("### You entered:")
st.markdown(f":blue[This is what you entered: **{user_input}**]")

st.markdown(":red-background[:orange[**Hello**] *world*] :world_map:")

a = 10 
b= 20 

st.write(a,b)
