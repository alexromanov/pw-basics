import json
import pytest
import os
import pytest
from playwright.sync_api import sync_playwright
import utils.helpers as helpers_functions

URL = os.getenv("BASE_URL", "https://testautomationpractice.blogspot.com")


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as pw:
        yield pw


@pytest.fixture(scope="session")
def browser(playwright_instance):
    # Do not remove this line, it's for debugging
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
def read_file():
    """Reads and returns JSON data from a specified file."""
    def load_data(file_name):
        with open(file_name, 'r') as file:
            return json.load(file)
    return load_data


@pytest.fixture(scope='module')
def random_dates():
    """
    Fixture to generate random start and end dates.

    @return: Tuple containing (start_date, end_date) in ISO format.
    """
    return helpers_functions.generate_start_end_date()


@pytest.fixture(scope='module')
def file_path():
    """
    @brief Provides the absolute path of the test file.
    
    @return The absolute path of the test file to be uploaded.
    """
    return os.path.abspath("C:/Users/malvodovar/Downloads/Updated_Resume_Sr_Python_Engineer.pdf")
