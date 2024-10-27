import streamlit as st
from utils import load_default_timetable, load_course_info, initialize_login_time, get_user_timezone, display_flip_clock, display_session_timer

def home_page():
    st.title("Welcome to Your Home Page")
    st.markdown("""Here, you can see your academic schedule and course information. Please find the slider on the left to access other features.""")

    st.markdown("<div style='text-align: center;'><h3>Current Time</h3><div id='flip-clock'></div></div>", unsafe_allow_html=True)
    display_flip_clock()
        
    st.markdown("<div style='text-align: center;'><h3>Session Timer</h3><div id='session-timer'></div></div>", unsafe_allow_html=True)
    display_session_timer()

    st.markdown(""" ### Academic Schedule and Course Information""")

    timetable_df = load_default_timetable()
    tab1, tab2 = st.tabs(["Weekly Schedule", "Course Information"])
    with tab1:
        st.subheader("Weekly Class Schedule")
        st.dataframe(timetable_df)
    with tab2:
        st.subheader("Course Information")
        course_info_df = load_course_info()
        st.dataframe(course_info_df)

initialize_login_time()
