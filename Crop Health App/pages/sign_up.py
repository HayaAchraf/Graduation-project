import streamlit as st
from database import add_user

def show():
    st.title("Sign-Up Page")
    username = st.text_input("Enter Username")
    password = st.text_input("Enter Password", type="password")
    if st.button("Sign Up"):
        add_user(username, password)
        st.success("User Registered Successfully!")