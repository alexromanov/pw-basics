import logging, pytest, random
from playwright.sync_api import expect


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

@pytest.mark.smoke
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

def test_radio_buttons(page):
    radio_buttons = page.locator('input[type=radio]')
    expect(radio_buttons).to_have_count(2)

    genders = ["male", "female"]
    selected = random.choice(genders)
    logger.info(f"Selected {selected} radio button")

    gender_radio = page.locator(f'xpath=//input[@id="{selected}"]')
    gender_radio.click()
    expect(gender_radio).to_be_checked()

def test_checkboxes(page):
    checkboxes = page.locator('input[type=checkbox]')
    expect(checkboxes).to_have_count(3)

    # select checkbox of the current day of the week and verify if is selected

def test_country_dropdown(page):
    # fix problem
    countries = page.locator("#countries")
    expect(countries).to_have_count(1)

    # select country by user locale and verify if is selected

def test_lists(page):
    ...
    # assert that colors has all expected values
    # select that animals has all expected values

def test_datepickers(page):
    ...
    # set date to 2024-12-31 using datepicker 1
    # set date to today date using datepicker 2
    # set date range from today to 2025-12-31 using datepicker 3

def test_upload_file(page):
    ...
    # upload a file using the file input

def test_upload_multiple_files(page):
    ...
    # upload multiple files using the file input

def test_static_web_table(page):
    ...

    # assert that the table has 7 rows and 4 columns
    # read all prices and calculate the total sum and average
    # read subjects and create a unique list of subjects

def test_pagination_table(page):
    ...
    # assert that the table has 20 rows and 4 columns
    # calculate total sum of all prices

def test_download_txt_file(page):
    ...
    # go to download file page (by the link in the footer)
    # enter file content, generate it, download and verify file content

def test_download_pdf_file(page):
    ...
    # go to download file page
    # download pdf file and verify file is saved and content is expected

def test_double_click(page):
    ...
    # double click on the button and verify the alert message

def test_mouse_hover(page):
    ...

    # hover over the button and verify the tooltip message options

def test_drap_and_drop(page):
    ...

    # drag and drop the element to the target and verify the message

def test_slider(page):
    ...

    # move the slider to the right and verify the value

def test_scroll_to_element(page):
    ...

    # scroll to the element 100 and verify if it is visible

def test_alerts(page):
    ...

    # click on the alert button and verify the alert message

def test_new_tab(page):
    ...

    # click on the new tab button and verify the new tab content
    # click on window popup button and verify the popup content

def test_dynamic_button(page):
    ...

    # click on the button and verify the dynamic content

def test_shadow_dom(page):
    ...

    # click on the checkbox, enter text and verify the shadow dom content

