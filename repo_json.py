"""Load ``events.json`` / ``workshops.json`` from GitHub when hosted on Streamlit Cloud.

Community Cloud can serve an older git checkout in the container until reboot; fetching
``raw.githubusercontent.com`` always reflects the latest commit after sheet sync.

Coordinates come from ``deploy.json`` via ``deploy_config`` (single source of truth).
"""

from __future__ import annotations

import os
import pathlib
import time
import urllib.error
import urllib.request

from deploy_config import get_github_coords

_ROOT = pathlib.Path(__file__).resolve().parent


def _raw_base_url() -> str | None:
    """Base URL without trailing slash, or None to read from disk only."""
    env = os.environ.get("NORTHSTAR_JSON_RAW_BASE", "").strip().rstrip("/")
    if env:
        return env
    try:
        from streamlit.runtime.scriptrunner import get_script_run_ctx
    except Exception:
        return None
    if get_script_run_ctx() is None:
        return None
    try:
        import streamlit as st

        try:
            v = st.secrets["NORTHSTAR_JSON_RAW_BASE"]
            if v:
                return str(v).strip().rstrip("/")
        except Exception:
            pass
        try:
            force = st.secrets.get("NORTHSTAR_FORCE_RAW_JSON", False)
            if str(force).lower() in ("1", "true", "yes"):
                owner, repo, branch = get_github_coords()
                return f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}"
        except Exception:
            pass
        host = (st.context.headers.get("Host") or st.context.headers.get("host") or "").lower()
        if ".streamlit.app" in host or ".streamlit.cloud" in host:
            owner, repo, branch = get_github_coords()
            return f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}"
    except Exception:
        pass
    return None


def read_repo_json(relative_path: str) -> str:
    """Return file text. Hosted Streamlit: GitHub raw; local dev: repo copy on disk."""
    if os.environ.get("NORTHSTAR_READ_JSON_FROM_DISK", "").lower() in ("1", "true", "yes"):
        return (_ROOT / relative_path).read_text(encoding="utf-8")

    base = _raw_base_url()
    if base:
        # Bust intermediaries that might reuse an older response for the same URL.
        bust = int(time.time() * 1000)
        url = f"{base}/{relative_path}?nocache={bust}"
        req = urllib.request.Request(
            url,
            headers={
                "User-Agent": "northstar-streamlit-json",
                "Cache-Control": "no-cache",
                "Pragma": "no-cache",
            },
            method="GET",
        )
        try:
            with urllib.request.urlopen(req, timeout=20) as resp:
                return resp.read().decode("utf-8")
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError):
            pass

    return (_ROOT / relative_path).read_text(encoding="utf-8")
