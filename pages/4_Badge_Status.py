import streamlit as st

from events import load_event_records

st.title("🏅 Badge status")

if "selected_event" not in st.session_state:
    st.session_state.selected_event = "None"

event = st.session_state["selected_event"]
records = load_event_records()

if not event or event == "None":
    st.warning("Select your event in the sidebar to see badge status.", icon="⚠️")
    st.stop()

if event not in records:
    st.error("That event is not in the list. Check the spelling or contact your workshop host.")
    st.stop()

status = records[event]["badges_issued"]

st.subheader(event)

if status is True:
    st.success(
        "**Badges have been issued** for this event. "
        "Check the email you used for your Snowflake trial (and spam/junk).",
        icon="✅",
    )
elif status is False:
    st.info(
        "**Badges are not issued yet** for this event. "
        "They are typically sent within **7 business days** after the workshop.",
        icon="🕐",
    )
else:
    st.warning(
        "**Status not published yet.** "
        "Your Snowflake team will update this page when badge sending has started or completed. "
        "Check again later.",
        icon="📋",
    )

st.divider()
st.markdown(
    "Questions about a missing badge? Email **developer-badges-DL@snowflake.com** "
    "(preferably within **30 days** of your event)."
)
