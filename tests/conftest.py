import json
import pytest
import os
import pytest
from playwright.sync_api import sync_playwright

URL = os.getenv("BASE_URL", "https://testautomationpractice.blogspot.com")


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as pw:
        yield pw


@pytest.fixture(scope="session")
def browser(playwright_instance):
    # browser = playwright_instance.chromium.launch(headless=False)
    browser = playwright_instance.chromium.launch(headless=True)
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto(URL)
    page.add_style_tag(content="""
        :root {
            --bg-color: #121212;
            --text-color: #e0e0e0;
            --link-color: #bb86fc;
        }
        body {
            background-color: var(--bg-color) !important;
            color: var(--text-color) !important;
        }
        a {
            color: var(--link-color) !important;
        }
    """)
    yield page
    context.close()


@pytest.fixture(scope='module')
def test_run_month_day_year_data():
    with open('test_run_month_day_year_data.json') as file:
        return json.load(file)


@pytest.fixture(scope='module')
def test_validation_month_day_year_data():
    with open('validation_month_day_year_data.json') as file:
        return json.load(file)

