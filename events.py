from __future__ import annotations

import csv
import io

import requests
import streamlit as st


@st.cache_data(ttl=3600)
def load_events() -> dict[str, str | None]:
    """Fetch events from a Google Sheet published as CSV.

    Expected columns: Event Name, Signup URL, Final URL.
    The app uses Final URL for the learner-facing link.
    """
    url = st.secrets["google_sheets"]["csv_url"]
    resp = requests.get(url, timeout=15)
    resp.raise_for_status()

    reader = csv.DictReader(io.StringIO(resp.text))
    events: dict[str, str | None] = {}
    for row in reader:
        name = row.get("Event Name", "").strip()
        if not name:
            continue
        final_url = row.get("Final URL", "").strip() or None
        events[name] = final_url
    return events
