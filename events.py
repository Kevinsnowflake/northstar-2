from __future__ import annotations

import json
import pathlib
from typing import Any

import streamlit as st

_EVENTS_FILE = pathlib.Path(__file__).parent / "events.json"


def _parse_badges_issued(raw: Any) -> bool | None:
    """Normalize JSON / sheet values to True (issued), False (not yet), or None (unknown)."""
    if raw is None:
        return None
    if isinstance(raw, bool):
        return raw
    if isinstance(raw, (int, float)):
        if raw == 1:
            return True
        if raw == 0:
            return False
        return None
    if isinstance(raw, str):
        s = raw.strip().lower()
        if s in ("yes", "true", "1", "y", "issued"):
            return True
        if s in ("no", "false", "0", "n", "not yet", "not_yet", "pending"):
            return False
        if s == "":
            return None
    return None


def load_event_records() -> dict[str, dict[str, Any]]:
    """Read events from events.json.

    Each value includes:
      - ``final_url``: str | None (trial signup link)
      - ``badges_issued``: bool | None — True if badges sent, False if not yet, None if unset
    """
    try:
        data = json.loads(_EVENTS_FILE.read_text())
        out: dict[str, dict[str, Any]] = {}
        for r in data:
            name = r.get("Event Name")
            if not name:
                continue
            name = str(name).strip()
            if not name:
                continue
            out[name] = {
                "final_url": r.get("Final URL") or None,
                "badges_issued": _parse_badges_issued(r.get("Badges issued")),
            }
        return out
    except (json.JSONDecodeError, KeyError, TypeError):
        st.warning("Could not load events — check events.json for formatting errors.", icon="⚠️")
        return {}
    except FileNotFoundError:
        return {}


def load_events() -> dict[str, str | None]:
    """Read events from events.json.

    Returns {event_name: final_url_or_None}.
    Falls back to an empty dict if the file is missing or malformed.
    """
    return {name: rec["final_url"] for name, rec in load_event_records().items()}
