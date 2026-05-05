# Northstar — operations

## Streamlit entrypoints

| Main file | Purpose |
|-----------|---------|
| `Home.py` | Primary Northstar app: `st.navigation`, sheet-driven JSON, all features. **Use this** for the main Community Cloud deployment. |
| `LegacyAutograderRedirect.py` | Only for a **separate** Streamlit app still bound to the legacy hostname `northstarautograder.streamlit.app`. It redirects browsers to the canonical `northstar.streamlit.app` (and preserves path/query). **Do not** set this as the main app’s entry if you want the full product. |
| `home_page.py` | Loaded as a **page** by `Home.py`, not run alone on Community Cloud (except backup / local experiments noted in code comments). |

After changing entrypoints, confirm each Community Cloud app’s **main file** in the deploy UI matches the row above.

## GitHub and sheet sync

- **Source of truth for repo coordinates:** `deploy.json` at the repository root (`github.owner`, `github.repo`, `github.branch`).
- **Python / Streamlit:** `deploy_config.py` and `repo_json.py` read `deploy.json` (with sensible defaults if the file is missing).
- **Google Apps Script (`apps_script.js`):** On each push, the script loads `deploy.json` from **raw GitHub** using `NORTHSTAR_DEPLOY_JSON_URL` (bootstrap URL). If that fetch fails, it falls back to `REPO_FALLBACK_*` constants — **keep those aligned with `deploy.json`** when you fork or rename the repo.
- When you **fork** or move the repo, update: `deploy.json`, `NORTHSTAR_DEPLOY_JSON_URL` in Apps Script, and the fallback constants in one pass.

## Data files (`events.json`, `workshops.json`)

- Updated by **Apps Script → GitHub Contents API** (see `apps_script.js`).
- The hosted app prefers **raw.githubusercontent.com** (see `repo_json.py`) so JSON changes do not depend on the container’s git checkout staying fresh.

## Cached JSON reads (Streamlit)

- ``events.py`` / ``workshops.py`` use ``@st.cache_data(ttl=15)`` on the raw JSON text so ``init_app`` and each page do not re-fetch on every fragment of the same rerun.
- After a sheet sync, new data can take **up to ~15 seconds** to appear without a manual refresh, or refresh immediately to start a new script run (cache is per-process).

## Local development

- Install: `pip install -r requirements.txt`
- Tests: `pip install -r requirements-dev.txt` then `pytest`
- To force disk-only JSON (no remote fetch): set environment variable `NORTHSTAR_READ_JSON_FROM_DISK=1`.
