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
    country_dropdown = page.locator('#country')
    country_dropdown.select_option(country_value)
    assert country_dropdown.input_value() == country_value,  f'Selected value is not {country_value}'

    selected_text = country_dropdown.locator('option:checked').text_content()
    assert selected_text.strip() == country_text, F'Displayed text is not {country_text}'
