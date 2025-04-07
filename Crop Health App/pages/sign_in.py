import streamlit as st
import sqlite3

def validate_user(username, password):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = c.fetchone()
    conn.close()
    return user

def show():
    st.title("Sign-In Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Log In"):
        if validate_user(username, password):
            st.success(f"Welcome, {username}!")
        else:
            st.error("Invalid credentials.")