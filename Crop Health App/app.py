import streamlit as st
import sqlite3
from pages import sign_in, sign_up, upload_image, view_history, admin_panel

st.sidebar.title("Navigation")
choice = st.sidebar.radio("Go to:", ["Sign Up", "Sign In", "Upload Image", "View History", "Admin Panel"])

if choice == "Sign Up":
    sign_up.show()
elif choice == "Sign In":
    sign_in.show()
elif choice == "Upload Image":
    upload_image.show()
elif choice == "View History":
    view_history.show()
elif choice == "Admin Panel":
    admin_panel.show()