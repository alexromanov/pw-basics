import logging, pytest


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


@pytest.mark.smoke
@pytest.mark.parametrize("name_input_value", ["Test"])
def test_name_input(page, name_input_value):
    name_input = page.locator("#name")
    name_input.fill(name_input_value)
    assert name_input.input_value() == "Test", f"Actual value is not equal to {name_input_value}"


@pytest.mark.smoke
@pytest.mark.parametrize("email_input_value", ["test@testson@mail.com"])
def test_email_input(page, email_input_value):
    email_input = page.locator("#email")
    email_input.fill(email_input_value)
    assert email_input.input_value() == "test@testson@mail.com", f"Actual value is not equal to {email_input_value}"


@pytest.mark.smoke
@pytest.mark.parametrize('phone_input_value', ["1234567890"])
def test_phone_input(page, phone_input_value):
    phone_input = page.locator("#phone")
    phone_input.fill(phone_input_value)
    assert phone_input.input_value() == "1234567890", f"Actual value is not equal to {phone_input_value}"


@pytest.mark.smoke
@pytest.mark.parametrize('text_input_value', ['Some text, with numbers 123!'])
def test_textarea_input(page, text_input_value):

    textarea_input = page.locator('#textarea')
    textarea_input.fill(text_input_value)
    assert textarea_input.input_value() == 'Some text, with numbers 123!', f'Actual value is not equal to {textarea_input}'
