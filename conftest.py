import os
import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

load_dotenv()

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p

@pytest.fixture
def api_request_context(playwright_instance):
    context = playwright_instance.request.new_context(
        base_url="https://reqres.in/api/",
        extra_http_headers={"x-api-key": os.getenv("REQRES_API_KEY")}
    )
    yield context
    context.dispose()

@pytest.fixture
def browser(playwright_instance):
    b = playwright_instance.chromium.launch(headless=True)
    yield b
    b.close()

@pytest.fixture
def page(browser):
    p = browser.new_page()
    yield p
    p.close()