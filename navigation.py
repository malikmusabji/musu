import streamlit as st
from home import home_page
from reading_material import reading_material_page
from simulation import simulation_page
from questions import questions_page
from attendance import attendance_page

import streamlit as st
from datetime import datetime

# Utility function to format time
def format_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return f"{hours:02d}:{minutes:02d}"

# Function to initialize or update the session state timer
def initialize_timer():
    if "start_time" not in st.session_state:
        st.session_state["start_time"] = datetime.now()
    if "elapsed_seconds" not in st.session_state:
        st.session_state["elapsed_seconds"] = 0

# Function to update the elapsed time in session state
def update_timer():
    if "start_time" in st.session_state:
        now = datetime.now()
        elapsed_time = (now - st.session_state["start_time"]).total_seconds()
        st.session_state["elapsed_seconds"] = int(elapsed_time)

# Dashboard UI function
def dashboard():
    st.title("Enhanced Student Dashboard")

    # Initialize timer if not already set
    initialize_timer()
    
    # Update timer on every interaction
    update_timer()
    
    # Display time spent
    st.subheader("Attendance Tracker")
    st.write("Time Spent on Site:", format_time(st.session_state["elapsed_seconds"]))

    # Reset timer button
    if st.button("Reset Timer"):
        st.session_state["start_time"] = datetime.now()
        st.session_state["elapsed_seconds"] = 0

# Run the dashboard function to display UI
dashboard()

def navigation():
    st.sidebar.title("Navigation")
    selected_page = st.sidebar.selectbox("Choose a page:", ["Home", "Reading Material", "Simulation", "Questions", "Attendance"])
    if st.sidebar.button("Logout"):
        st.session_state.login_status = False
        st.session_state.pop('login_time', None)
        st.success("You have been logged out.")
    if selected_page == "Home":
        home_page()
    elif selected_page == "Reading Material":
        reading_material_page()
    elif selected_page == "Simulation":
        simulation_page()
    elif selected_page == "Questions":
        questions_page()
    elif selected_page == "Attendance":
        attendance_page()
