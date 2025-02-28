import json
import sys
import pytest
import os
import pytest
from playwright.sync_api import sync_playwright
import utils.helpers as helpers_functions

PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

URL = os.getenv("BASE_URL", "https://testautomationpractice.blogspot.com")


def pytest_addoption(parser):
    """
    Adds a CLI argument '--browser-visible' for controlling browser mode.
    """
    parser.addoption(
        '--browser-visible',
        action='store_true',
        default=False,
        help="Run tests with the browser UI (headed mode). Default is headless mode."
    )


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as pw:
        yield pw


@pytest.fixture(scope="session")
def browser(playwright_instance, request):
    """
    Provides a Playwright browser instance with dynamic headless control.
    @usage
    ```
    Run in headed mode (browser UI visible):
    pytest --browser-visible
    pytest 'tests/test_inputs.py::test_textarea_input[Some text, with numbers 123!]' --browser-visible
    Run in headless mode (default):
    pytest
    pytest 'tests/test_inputs.py::test_textarea_input[Some text, with numbers 123!]'
    ```
    If running via PyCharm Run Button, it checks the `BROWSER_VISIBLE` environment variable.
    """

    cli_headed = request.config.getoption("--browser-visible")
    env_headed = os.getenv("BROWSER_VISIBLE", "false").lower() == 'true'
    headless_mode = not (cli_headed or env_headed)

    browser = playwright_instance.chromium.launch(headless=headless_mode)
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
        abs_path = os.path.abspath(file_name)  # Convert to absolute path
        with open(abs_path, 'r') as file:
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
