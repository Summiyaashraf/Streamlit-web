import streamlit as st

st.title("Simple Stramlit App")
user_input = st.text_input("Enter some text:")

if st.button("Show Text"):
    st.write(f"You entered: {user_input}")
    