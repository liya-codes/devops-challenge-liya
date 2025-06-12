# tests/test_api.py
import os
import requests


PORT = os.getenv("PORT", "5000")          # overridable via env
BASE = f"http://localhost:5001"         # common base URL


def test_health():
    """`/health` should return 200 and the expected container/project/status fields."""
    resp = requests.get(f"{BASE}/health", timeout=5)
    assert resp.status_code == 200

    body = resp.json()
    # Presence checks
    assert body.get("status") == "healthy"
    assert body.get("container"),  "missing 'container' field"
    assert body.get("project"),    "missing 'project' field"


def test_secret():
    """`/secret` should return 200 and include a non-empty secret_code value."""
    resp = requests.get(f"{BASE}/secret", timeout=5)
    assert resp.status_code == 200

    body = resp.json()
    assert "secret_code" in body, "key 'secret_code' not in response"
    assert body["secret_code"],   "'secret_code' is empty"
