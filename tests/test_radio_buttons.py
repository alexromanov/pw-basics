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
def test_radio_buttons(page, radio_button_id):
    radio_button = page.locator(radio_button_id)
    radio_button.click()
    expect(radio_button).to_be_checked()




