import logging, pytest, random
import allure
from playwright.sync_api import expect


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

@pytest.mark.smoke
@allure.title("Test Inputs")
@allure.tag("practice")
@allure.severity(allure.severity_level.CRITICAL)
def test_inputs(page):
    name = page.locator("#name")
    expect(name).to_be_empty()
    name.fill("Test")

    email = page.locator("#email")
    expect(email).to_be_empty()
    email.fill("test@testson@mail.com")

    phone = page.locator("#phone")
    phone.fill("1234567890")
    expect(phone).to_have_value("1234567890")
    assert phone == "1234567890", f"Phone number is not correct"

@allure.title("Test Radio Buttons")
@allure.tag("practice")
@allure.severity(allure.severity_level.CRITICAL)
def test_radio_buttons(page):
    radio_buttons = page.locator('input[type=radio]')
    expect(radio_buttons).to_have_count(2)

    genders = ["male", "female"]
    selected = random.choice(genders)
    logger.info(f"Selected {selected} radio button")

    gender_radio = page.locator(f'xpath=//input[@id="{selected}"]')
    gender_radio.click()
    expect(gender_radio).to_be_checked()

@allure.title("Test Checkboxes")
@allure.tag("practice")
@allure.severity(allure.severity_level.CRITICAL)
def test_checkboxes(page):
    checkboxes = page.locator('input[type=checkbox]')
    expect(checkboxes).to_have_count(3)

    # select checkbox of the current day of the week and verify if is selected

@allure.title("Test Dropdown")
@allure.tag("practice")
@allure.severity(allure.severity_level.CRITICAL)
def test_country_dropdown(page):
    # fix problem
    countries = page.locator("#countries")
    expect(countries).to_have_count(1)

    # select country by user locale and verify if is selected

@allure.title("Test Lists")
@allure.tag("practice")
@allure.severity(allure.severity_level.CRITICAL)
def test_lists(page):
    ...
    # assert that colors has all expected values
    # select that animals has all expected values

@allure.title("Test Datepickers")
@allure.tag("practice")
@allure.severity(allure.severity_level.CRITICAL)
def test_datepickers(page):
    ...
    # set date to 2024-12-31 using datepicker 1
    # set date to today date using datepicker 2
    # set date range from today to 2025-12-31 using datepicker 3

@allure.title("Test Upload File")
@allure.tag("practice")
@allure.severity(allure.severity_level.CRITICAL)
def test_upload_file(page):
    ...
    # upload a file using the file input

@allure.title("Test Multiple Upload Files")
@allure.tag("practice")
@allure.severity(allure.severity_level.CRITICAL)
def test_upload_multiple_files(page):
    ...
    # upload multiple files using the file input

@allure.title("Test Web Tables")
@allure.tag("practice")
@allure.severity(allure.severity_level.CRITICAL)
def test_static_web_table(page):
    ...

    # assert that the table has 7 rows and 4 columns
    # read all prices and calculate the total sum and average
    # read subjects and create a unique list of subjects

@allure.title("Test Pagination Table")
@allure.tag("practice")
@allure.severity(allure.severity_level.CRITICAL)
def test_pagination_table(page):
    ...
    # assert that the table has 20 rows and 4 columns
    # calculate total sum of all prices

@allure.title("Test Download Files")
@allure.tag("practice")
@allure.severity(allure.severity_level.CRITICAL)
def test_download_txt_file(page):
    ...
    # go to download file page (by the link in the footer)
    # enter file content, generate it, download and verify file content

@allure.title("Test Download Pdf Files")
@allure.tag("practice")
@allure.severity(allure.severity_level.CRITICAL)
def test_download_pdf_file(page):
    ...
    # go to download file page
    # download pdf file and verify file is saved and content is expected

@allure.title("Test Double Click")
@allure.tag("practice")
@allure.severity(allure.severity_level.CRITICAL)
def test_double_click(page):
    ...
    # double click on the button and verify the alert message

@allure.title("Test Mouse Hover")
@allure.tag("practice")
@allure.severity(allure.severity_level.CRITICAL)
def test_mouse_hover(page):
    ...

    # hover over the button and verify the tooltip message options

@allure.title("Test Drag and Drop")
@allure.tag("practice")
@allure.severity(allure.severity_level.CRITICAL)
def test_drap_and_drop(page):
    ...

    # drag and drop the element to the target and verify the message

@allure.title("Test Inputs")
@allure.tag("practice")
@allure.severity(allure.severity_level.CRITICAL)
def test_slider(page):
    ...

    # move the slider to the right and verify the value

@allure.title("Test Scroll")
@allure.tag("practice")
@allure.severity(allure.severity_level.CRITICAL)
def test_scroll_to_element(page):
    ...

    # scroll to the element 100 and verify if it is visible

@allure.title("Test Alerts")
@allure.tag("practice")
@allure.severity(allure.severity_level.CRITICAL)
def test_alerts(page):
    ...

    # click on the alert button and verify the alert message

@allure.title("Test New Tab")
@allure.tag("practice")
@allure.severity(allure.severity_level.CRITICAL)
def test_new_tab(page):
    ...

    # click on the new tab button and verify the new tab content
    # click on window popup button and verify the popup content

@allure.title("Test Dynamic Button")
@allure.tag("practice")
@allure.severity(allure.severity_level.CRITICAL)
def test_dynamic_button(page):
    ...

    # click on the button and verify the dynamic content

@allure.title("Test Shadow Dom")
@allure.tag("practice")
@allure.severity(allure.severity_level.CRITICAL)
def test_shadow_dom(page):
    ...

    # click on the checkbox, enter text and verify the shadow dom content

