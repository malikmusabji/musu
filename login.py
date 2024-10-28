import streamlit as st
import sqlite3

 def login_page():
    st.markdown("<h1 style='text-align: center; color: #ff5733;'>PedoMUS</h1>", unsafe_allow_html=True)
    st.markdown("""
    ### Welcome to PedoMUS
    **PedoMUS** is a comprehensive educational dashboard that provides an array of tools to support effective learning. The platform allows users to track and manage attendance with ease, interact with uploaded PPTs and PDFs through an intelligent chatbot that can summarize and explain content, and generate multiple-choice questions based on notes to aid in self-assessment. Additionally, PedoMUS offers access to simulation tools that facilitate a deeper understanding of complex concepts. Together, these features create an integrated, user-friendly environment to enrich the educational experience.
    """)
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = c.fetchone()
        conn.close()

        if user:
            st.session_state.login_status = True
            st.success("Logged in successfully!")
        else:
            st.error("Invalid username or password.")
