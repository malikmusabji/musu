import streamlit as st
import pandas as pd
import pytz
import requests
from datetime import datetime

@st.cache_data
def load_default_timetable():
    data = {
        "Time": ["09-10 AM", "10-11 AM", "11-12 AM", "12-01 PM", "01-02 PM", "02-03 PM", "03-04 PM", "04-05 PM"],
        "Monday": ["Lecture / G:All C:PEV112 / R: 56-703 / S:BO301", "Lecture / G:All C:PEA402 / R: 56-605 / S:BO301", "Lecture / G:All C:BTY496 / R: 56-708 / S:B2201", "", "Lecture / G:All C:BTY463 / R: 56-809 / S:B2201", "", "Lecture / G:All C:BTY441 / R: 56-801 / S:BM302", ""],
        "Tuesday": ["Lecture / G:All C:PEV112 / R: 56-703 / S:BO301", "Lecture / G:All C:PEA402 / R: 56-605 / S:BO301", "Lecture / G:All C:BTY496 / R: 56-607 / S:B2201", "", "Lecture / G:All C:BTY651 / R: 56-710 / S:BE098", "", "", ""],
        "Wednesday": ["Practical / G:1 C:PEV112 / R: 56-703 / S:BO301", "Practical / G:1 C:PEV112 / R: 56-703 / S:BO301", "Lecture / G:All C:BTY651 / R: 56-710 / S:BE098", "Lecture / G:All C:BTY651 / R: 56-609 / S:BE098", "Lecture / G:All C:BTY396 / R: 56-710 / S:B2201", "", "", ""],
        "Thursday": ["", "", "", "Lecture / G:All C:BTY441 / R: 56-707 / S:BM302", "", "Tutorial / G:1 C:PEA402 / R: 56-509 / S:BO301", "", ""],
        "Friday": ["", "", "", "", "", "", "", ""]
    }
    return pd.DataFrame(data)

@st.cache_data
def load_course_info():
    course_data = {
        "CourseCode": ["BTY396", "BTY416", "BTY441", "BTY463", "BTY464", "BTY496", "BTY499", "BTY651", "ICT202B", "PEA402", "PEMS07", "PESS01", "PEV112"],
        "CourseType": ["CR", "CR", "EM", "CR", "CR", "CR", "CR", "PW", "CR", "OM", "PE", "PE", "OM"],
        "CourseName": ["BIOSEPARATION ENGINEERING", "BIOSEPARATION ENGINEERING LABORATORY", "PHARMACEUTICAL ENGINEERING", "BIOINFORMATICS AND COMPUTATIONAL BIOLOGY", "BIOINFORMATICS AND COMPUTATIONAL BIOLOGY LABORATORY", "METABOLIC ENGINEERING", "SEMINAR ON SUMMER TRAINING", "QUALITY CONTROL AND QUALITY ASSURANCE", "AI, ML AND EMERGING TECHNOLOGIES", "ANALYTICAL SKILLS -II", "MENTORING - VII", "SOFTSKILLS - I", "VERBAL ABILITY"],
        "Credits": [3, 1, 3, 2, 1, 2, 3, 3, 2, 4, 0, 0, 3],
        "Faculty": ["Dr. Ajay Kumar", "Dr. Ajay Kumar", "Dr. Shashank Garg", "Dr. Anish Kumar", "Dr. Anish Kumar", "Dr. Shashank Garg", "", "Dr. Aarti Bains", "Dr. Piyush Kumar Yadav", "Kamal Deep", "", "Ayush Srivastava", "Jaskiranjit Kaur"]
    }
    return pd.DataFrame(course_data)

def get_llminfo():
    st.sidebar.header("Options", divider='rainbow')
    model = st.sidebar.radio("Choose LLM:", ("gemini-1.5-pro", "gemini-1.5-flash", "gemini-1.5-standard", "gemini-1.5-advanced"))
    temperature = st.sidebar.slider("Temperature:", 0.0, 2.0, 1.0, 0.25)
    top_p = st.sidebar.slider("Top P:", 0.0, 1.0, 0.94, 0.01)
    max_tokens = st.sidebar.slider("Maximum Tokens:", 100, 5000, 2000, 100)
    top_k = st.sidebar.slider("Top K:", 0, 100, 50, 1)
    return model, temperature, top_p, max_tokens, top_k


def get_user_timezone():
    try:
        response = requests.get("https://ipinfo.io/json")
        if response.status_code == 200:
            data = response.json()
            return data.get("timezone", "UTC")
    except Exception as e:
        st.error(f"Failed to fetch timezone: {e}")
    return "UTC"

def display_session_timer():
    elapsed_time = (datetime.now(pytz.timezone(get_user_timezone())) - st.session_state.login_time).total_seconds()
    session_timer_html = f"""
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/flipclock/0.7.8/flipclock.min.css">
        <div id="session-timer" style="display: flex; justify-content: center;"></div>
        
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/flipclock/0.7.8/flipclock.min.js"></script>
        <script type="text/javascript">
            document.addEventListener("DOMContentLoaded", function() {{
                var timer = new FlipClock(document.getElementById('session-timer'), {{
                    clockFace: 'MinuteCounter',
                    autoStart: true
                }});
                // Set the timer to start from the elapsed time
                timer.setTime({int(elapsed_time)});
                timer.start();
            }});
        </script>
        """
    st.components.v1.html(session_timer_html, height=100)

def display_flip_clock():
    user_timezone = get_user_timezone()
    flipclock_html = f"""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/flipclock/0.7.8/flipclock.min.css">
    <div id="flip-clock" style="display: flex; justify-content: center;"></div>
    
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/flipclock/0.7.8/flipclock.min.js"></script>
    <script type="text/javascript">
        document.addEventListener("DOMContentLoaded", function() {{
            var clock = new FlipClock(document.getElementById('flip-clock'), {{
                clockFace: 'TwentyFourHourClock',
                showSeconds: true
            }});
        }});
    </script>
    """

    st.components.v1.html(flipclock_html, height=100)

def initialize_login_time():
    if "login_time" not in st.session_state:
        st.session_state.login_time = datetime.now(pytz.timezone(get_user_timezone()))

def detect_tab_switch():
    js_code = """
    <script>
        let tabSwitchCount = 0;

        document.addEventListener("visibilitychange", function() {
            if (document.hidden) {
                tabSwitchCount++;
                if (tabSwitchCount >= 3) {
                    alert("You have switched tabs 3 times. The page will now close.");
                    window.close();  // Close the website after 3 tab switches
                } else {
                    alert("Warning: You have switched tabs " + tabSwitchCount + " times. The page will close after 3 switches.");
                }
            }
        });
    </script>
    """
    st.components.v1.html(js_code, height=0, scrolling=False)
