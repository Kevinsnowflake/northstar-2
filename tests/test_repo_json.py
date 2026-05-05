from __future__ import annotations

import pytest


def test_read_repo_json_events_disk_mode(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("NORTHSTAR_READ_JSON_FROM_DISK", "1")
    try:
        from repo_json import read_repo_json

        text = read_repo_json("events.json")
    finally:
        monkeypatch.delenv("NORTHSTAR_READ_JSON_FROM_DISK", raising=False)
    assert text.strip().startswith("[")
