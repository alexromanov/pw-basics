import logging, pytest
from playwright.sync_api import expect

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


@pytest.mark.smoke
@pytest.mark.parametrize('radio_button_id', ['#male',
                                             '#female',
                                             '#sunday',
                                             '#monday',
                                             '#tuesday',
                                             '#wednesday',
                                             '#thursday',
                                             '#friday',
                                             '#saturday'])
def test_days_radio_buttons(page, radio_button_id):
    """
    1. Locate the radio button using its ID.
    2. Click the radio button to select it.
    3. Verify that the clicked radio button is checked.
    """

    radio_button = page.locator(radio_button_id)
    radio_button.click()

    expect(radio_button).to_be_checked()


@pytest.mark.smoke
@pytest.mark.parametrize('radio_button_id', ['#male', '#female'])
def test_gender_radio_button(page, radio_button_id):
    """
    1. Locate the radio button element using its ID.
    2. Click the radio button to select it.
    3. Verify that the selected radio button is checked.
    """

    radio_button = page.locator(radio_button_id)
    radio_button.click()

    expect(radio_button).to_be_checked()
