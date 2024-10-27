import streamlit as st
import google.generativeai as genai
from db import init_db
from navigation import navigation
from login import login_page
from utils import get_user_timezone, detect_tab_switch

detect_tab_switch()
genai.configure(api_key=st.secrets["API_KEY"])
get_user_timezone()
init_db()

if "login_status" not in st.session_state:
    st.session_state.login_status = False  

if st.session_state.login_status:
    navigation()  
else:
    login_page() 

