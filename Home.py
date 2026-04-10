import streamlit as st
from events import load_events

st.set_page_config(page_title="Snowflake Northstar", page_icon="❄️", layout="wide")

EVENTS = load_events()
EVENT_OPTIONS = ["None"] + list(EVENTS.keys())

if "selected_event" not in st.session_state:
    st.session_state.selected_event = "None"

with st.sidebar:
    st.selectbox("Select your event", EVENT_OPTIONS, key="selected_event")

pages = [
    st.Page("home_page.py", title="Home", icon="❄️", default=True),
    st.Page("pages/1_Trial_Sign_Up.py", title="Trial Sign Up", icon="📝"),
    st.Page("pages/2_Guides_and_Answer_Keys.py", title="Guides & Answer Keys", icon="📚"),
    st.Page("pages/3_Auto-Grader.py", title="Auto-Grader", icon="⚙️"),
]

nav = st.navigation(pages)
nav.run()
