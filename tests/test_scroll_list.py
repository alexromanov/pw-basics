import logging, pytest


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


@pytest.mark.smoke
@pytest.mark.parametrize('list_option_value, list_text', [
    ('red', 'Red'),
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('yellow', 'Yellow'),
    ('red', 'Red'),
    ('white', 'White'),
    ('green', 'Green')
])
def test_scroll_list_color(page, list_option_value, list_text):
    scroll_list = page.locator('#colors')
    scroll_list.select_option(list_option_value)
    assert scroll_list.input_value() == list_option_value, f'Selected value is not {list_option_value}'

    selected_text = scroll_list.locator('option:checked').text_content()
    assert ''.join(selected_text.split()) == list_text, F'Displayed text is not {list_text}'


@pytest.mark.smoke
@pytest.mark.parametrize('list_option_value, list_text', [
    ('cat', 'Cat'),
    ('cheetah', 'Cheetah'),
    ('deer', 'Deer'),
    ('dog', 'Dog'),
    ('elephant', 'Elephant'),
    ('fox', 'Fox'),
    ('giraffe', 'Giraffe'),
    ('lion', 'Lion'),
    ('rabbit', 'Rabbit'),
    ('zebra', 'Zebra')
])
def test_scroll_list_sorted(page, list_option_value, list_text):
    sorted_list = page.locator('#animals')
    sorted_list.select_option(list_option_value)
    assert sorted_list.input_value() == list_option_value, f'Selected value is not {list_option_value}'

    selected_text = sorted_list.locator('option:checked').text_content()
    assert ''.join(selected_text.split()) == list_text, F'Displayed text is not {list_text}'

