import logging
import pytest

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


@pytest.mark.smoke
@pytest.mark.parametrize('country_value, country_text', [
    ("usa", "United States"),
    ("canada", "Canada"),
    ("uk", "United Kingdom"),
    ("germany", "Germany"),
    ("france", "France"),
    ("australia", "Australia"),
    ("japan", "Japan"),
    ("china", "China"),
    ("brazil", "Brazil"),
    ("india", "India"),])
def test_select_countries(page, country_value, country_text):
    """
    1. Locate the country dropdown element using its selector `#country`.
    2. Select the country using the provided `country_value`.
    3. Retrieve and validate that the dropdown's input value matches `country_value`.
    4. Find the currently selected option text.
    5. Assert that the displayed option text matches the expected `country_text`.
    """

    country_dropdown = page.locator('#country')
    country_dropdown.select_option(country_value)
    assert country_dropdown.input_value() == country_value,  f'Selected value is not {country_value}'

    selected_text = country_dropdown.locator('option:checked').text_content()
    assert selected_text.strip() == country_text, F'Displayed text is not {country_text}'
