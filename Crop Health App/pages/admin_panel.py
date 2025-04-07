import streamlit as st
import sqlite3

def remove_user(username):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("DELETE FROM users WHERE username=?", (username,))
    conn.commit()
    conn.close()

def show():
    st.title("Admin Panel")
    username = st.text_input("Enter Username to Remove")
    if st.button("Delete User"):
        remove_user(username)
        st.success(f"User {username} deleted successfully!")