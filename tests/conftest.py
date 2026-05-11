import os
import subprocess
import sys
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


BASE_URL = "http://127.0.0.1:5000"


def _wait_for_server(url: str, timeout: int = 20) -> None:
    import urllib.request

    start = time.time()
    while time.time() - start < timeout:
        try:
            with urllib.request.urlopen(url):  # nosec B310
                return
        except Exception:
            time.sleep(0.5)
    raise RuntimeError("Flask server did not start in time")


@pytest.fixture(scope="session", autouse=True)
def flask_server():
    process = subprocess.Popen(
        [sys.executable, "app.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env={**os.environ, "PYTHONUNBUFFERED": "1"},
    )
    try:
        _wait_for_server(BASE_URL)
        yield
    finally:
        process.terminate()
        process.wait(timeout=10)


@pytest.fixture
def browser():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1366,768")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(3)
    yield driver
    driver.quit()
