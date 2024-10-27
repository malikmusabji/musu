import streamlit as st
from home import home_page
from reading_material import reading_material_page
from simulation import simulation_page
from questions import questions_page
from attendance import attendance_page

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
