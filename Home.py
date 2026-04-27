import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Redirecting…", layout="centered")

TARGET = "https://northstar.streamlit.app"

components.html(
    f"""
    <script>
      window.top.location.href = "{TARGET}";
    </script>
    <noscript>
      <meta http-equiv="refresh" content="0; url={TARGET}">
    </noscript>
    <p style="font-family: system-ui;">
      If you are not redirected automatically,
      <a href="{TARGET}">open Northstar here</a>.
    </p>
    """,
    height=120,
)
