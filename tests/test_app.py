import requests
import os

def test_health():
    port = os.getenv("PORT", "5000")             # uses $PORT or defaults to 5000
    url = f"http://localhost:{port}/health"

    response = requests.get(url, timeout=5)      # 5-second safety timeout
    assert response.status_code == 200



def test_health():
    port = os.getenv("PORT", "5000")             # uses $PORT or defaults to 5000
    url = f"http://localhost:{port}/health"

    response = requests.get(url, timeout=5)      # 5-second safety timeout
    assert response.status_code == 200