import pytest
import requests
import os

def test_secret():
    port = os.getenv("PORT", "5000")             # uses $PORT or defaults to 5000
    url = f"http://0.0.0.0:{port}/secret"

    response = requests.get(url, timeout=5)      # 5-second safety timeout
    assert response.status_code == 200