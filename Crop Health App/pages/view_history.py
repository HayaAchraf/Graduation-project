import streamlit as st
import sqlite3

def get_images():
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("SELECT * FROM images")
    data = c.fetchall()
    conn.close()
    return data

def show():
    st.title("Image Classification History")
    data = get_images()
    st.table(data)