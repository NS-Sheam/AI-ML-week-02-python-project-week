# Create a calculator using Streamlit:
# Two number inputs
# A selectbox for operations (+, -, *, /)
# Display the result when a button is clicked


import streamlit as st

st.title("Simple Calculator", anchor=False, width=400)

num1 = st.number_input("Enter the first number", value=None, placeholder="Type the first number...")
num2 = st.number_input("Enter the second number", value=None, placeholder="Type the second number...")

operation = st.selectbox("Select an operation", ("+", "-", "*", "/"))

btn = st.button("Calculate", type="primary")

if btn:
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("Cannot divide by zero")
            result = None

    if result is not None:
        st.success(f"The result of {num1} {operation} {num2} is: {result}")
        st.balloons() # Celebrate the calculation with balloons!