import logging, pytest


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


@pytest.mark.smoke
@pytest.mark.parametrize('list_id, list_option_value, list_text', [
    ('#colors', 'red', 'Red'),
    ('#colors', 'blue', 'Blue'),
    ('#colors', 'green', 'Green'),
    ('#colors', 'yellow', 'Yellow'),
    ('#colors', 'red', 'Red'),
    ('#colors', 'white', 'White'),
    ('#colors', 'green', 'Green'),
    ('#animals', 'cat', 'Cat'),
    ('#animals', 'cheetah', 'Cheetah'),
    ('#animals', 'deer', 'Deer'),
    ('#animals', 'dog', 'Dog'),
    ('#animals', 'elephant', 'Elephant'),
    ('#animals', 'fox', 'Fox'),
    ('#animals', 'giraffe', 'Giraffe'),
    ('#animals', 'lion', 'Lion'),
    ('#animals', 'rabbit', 'Rabbit'),
    ('#animals', 'zebra', 'Zebra')
])
def test_scroll_list(page, list_id, list_option_value, list_text):
    """
    @brief Verifies that a scrollable list correctly selects an option and displays the expected text.

    @param page The Playwright page instance.
    @param list_id The ID of the list element being tested.
    @param list_option_value The value of the option to select.
    @param list_text The expected text of the selected option.

    @test
    1. Locate the specified scrollable list by its ID.
    2. Select an option by value.
    3. Verify that the selected option value matches the expected value.
    4. Verify that the displayed text of the selected option matches the expected text.

    @assert The selected value should match the expected option value.
    @assert The displayed text should match the expected option text.
    """

    scroll_list = page.locator(list_id)
    scroll_list.select_option(list_option_value)

    # Validate selected value
    assert scroll_list.input_value() == list_option_value, f'Selected value is not {list_option_value}'

    # Validate displayed text
    selected_text = scroll_list.locator('option:checked').text_content()
    assert ''.join(selected_text.split()) == list_text, f'Displayed text is not {list_text}'
