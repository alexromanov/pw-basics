import os, pytest
from playwright.sync_api import sync_playwright

URL = os.getenv("BASE_URL", "https://testautomationpractice.blogspot.com")

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as pw:
        yield pw

@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=True)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto(URL)
    yield page
    context.close()