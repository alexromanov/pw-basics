import time
from datetime import datetime

import pytest
import logging
from playwright.sync_api import expect
import utils.helpers as helpers_functions

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


@pytest.mark.smoke
def test_date_picker_selection(page, read_file):
    """
    1. Open the date picker by clicking the input field.
    2. Determine whether to test month or year selection.
    3. Select the desired option using the dropdown.
    4. Verify that the selected value matches the expected value.
    5. Verify that the displayed text matches the expected representation.
    """

    select_mont_day_year_validation_data = read_file('select_mont_day_year_validation_data.json')['date_picker_options']

    txt_date = page.locator('#txtDate')
    txt_date.click()

    for valid_data_dict in select_mont_day_year_validation_data:
        select_type = valid_data_dict['select_type']
        list_option_value = valid_data_dict['list_option_value']
        list_text = valid_data_dict['list_text']

        if select_type == 'month':
            date_picker_selector = page.locator('.ui-datepicker-month')
        else:
            date_picker_selector = page.locator('.ui-datepicker-year')

        date_picker_selector.select_option(list_option_value)

        assert date_picker_selector.input_value() == list_option_value, f"Selected value is not {list_option_value}"

        selected_text = date_picker_selector.locator('option:checked').text_content()
        assert ''.join(selected_text.split()) == list_text, f"Displayed text is not {list_text}"


@pytest.mark.smoke
def test_full_date(page, read_file):
    """
    1. Load test data for date selection and expected validation data.
    2. Iterate through years, months, and days in the test data.
    3. Open the date picker and select the appropriate year, month, and day.
    4. Verify that the input field displays the correct date.
    5. Validate the result against expected test validation data.
    """

    run_month_day_year_data = read_file('year_month_days_validation_data.json')
    validation_month_day_year_data = read_file('year_month_full_dates_validation_data.json')

    txt_date = page.locator('#txtDate')

    current_year = datetime.now().year
    min_year = current_year - 0
    max_year = current_year + 0

    for year, months in run_month_day_year_data.items():
        if not (min_year <= int(year) <= max_year):
            continue  # Skip years outside range

        for month, expected_dates in months.items():
            for day in expected_dates:
                txt_date.click()

                year_locator = page.locator('.ui-datepicker-year')
                month_locator = page.locator('.ui-datepicker-month')

                year_locator.select_option(year)
                month_locator.select_option(str(helpers_functions.month_name_to_index(month)))

                date_locator = page.locator(f".ui-datepicker-calendar td[data-handler='selectDay'] a[data-date='{day}']")
                date_locator.click()

                actual_date_str = txt_date.input_value()

                expected_validation_date = validation_month_day_year_data.get(year, {}).get(month, [])[int(day) - 1]

                assert expected_validation_date, f"Missing validation data for {day} {month} {year}."
                assert actual_date_str == expected_validation_date, (
                    f"Date mismatch! Expected: {expected_validation_date}, Got: {actual_date_str}"
                )


@pytest.mark.smoke
def test_next_month_year(page, read_file):
    """
    1. Open the date picker by clicking the input field.
    2. Retrieve the currently selected month and year.
    3. Click 'Next' multiple times to navigate through months.
    4. Verify that the displayed month and year correctly update.
    """
    run_month_day_year_data = read_file('year_month_days_validation_data.json')

    txt_date = page.locator('#txtDate')
    txt_date.click()

    year_locator = page.locator('.ui-datepicker-year')
    month_locator = page.locator('.ui-datepicker-month')

    start_year = year_locator.locator('option[selected]').text_content()
    start_moth = month_locator.locator('option[selected]').text_content()

    expected_dates = [
        (year, month) for year, month in run_month_day_year_data.items() for month in month.keys()
    ]

    index = expected_dates.index((start_year, start_moth))

    for click_next in range(24):
        page.locator('.ui-datepicker-next').click()
        index = (index + 1) % len(expected_dates)
        current_year = year_locator.locator('option[selected]').text_content()
        current_month = month_locator.locator('option[selected]').text_content()

        expected_year, expected_month = expected_dates[index]

        assert current_year == expected_year, f"Year mismatch: expected {expected_year}, got {current_year}"
        assert current_month == current_month, f"Month mismatch: expected {expected_month}, got {current_month}"


@pytest.mark.smoke
def test_prev_month_year(page, read_file):
    """
    1. Open the date picker by clicking the input field.
    2. Retrieve the currently selected month and year.
    3. Click 'Previous' multiple times to navigate through months.
    4. Verify that the displayed month and year correctly update.
    """

    run_month_day_year_data = read_file('year_month_days_validation_data.json')

    text_date = page.locator('#txtDate')
    text_date.click()

    year_locator = page.locator('.ui-datepicker-year')
    month_locator = page.locator('.ui-datepicker-month')

    start_year = year_locator.locator('option[selected]').text_content()
    start_moth = month_locator.locator('option[selected]').text_content()

    expected_dates = [
        (year, month) for year, month in run_month_day_year_data.items() for month in month.keys()
    ]

    index = expected_dates.index((start_year, start_moth))

    for click_prev in range(24):
        page.locator('.ui-datepicker-prev').click()
        index = (index - 1) % len(expected_dates)
        current_year = year_locator.locator('option[selected]').text_content()
        current_month = month_locator.locator('option[selected]').text_content()

        expected_year, expected_month = expected_dates[index]

        assert current_year == expected_year, f"Year mismatch: expected {expected_year}, got {current_year}"
        assert current_month == expected_month, f"Month mismatch: expected {expected_month}, got {current_month}"


@pytest.mark.smoke
@pytest.mark.parametrize('day_id, day_value', [
    ('Su', 'Sunday'),
    ('Mo', 'Monday'),
    ('Tu', 'Tuesday'),
    ('We', 'Wednesday'),
    ('Th', 'Thursday'),
    ('Fr', 'Friday'),
    ('Sa', 'Saturday')
])
def test_week_days(page, day_id, day_value):
    """
    1. Open the date picker by clicking the input field.
    2. Retrieve the displayed weekday headers.
    3. Verify that the expected short and full weekday names are present.
    """

    text_locator = page.locator('#txtDate')
    text_locator.click()

    day_headers = page.locator('.ui-datepicker-calendar thead th span')

    values_days = [header.get_attribute('title') for header in day_headers.all()]
    assert day_value in values_days, f"Expected short day '{day_value}' not found in {values_days}"

    id_days = [header.text_content() for header in day_headers.all()]
    assert day_id in id_days, f"Expected short day '{day_id}' not found in {id_days}"
