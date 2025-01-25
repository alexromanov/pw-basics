import time
from datetime import datetime

import pytest
import logging
from playwright.sync_api import expect
import utils.helpers as helpers_functions

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


@pytest.mark.smoke
@pytest.mark.parametrize('list_option_value, list_text', [
    ('0', 'Jan'),
    ('1', 'Feb'),
    ('2', 'Mar'),
    ('3', 'Apr'),
    ('4', 'May'),
    ('5', 'Jun'),
    ('6', 'Jul'),
    ('7', 'Aug'),
    ('8', 'Sep'),
    ('9', 'Oct'),
    ('10', 'Nov'),
    ('11', 'Dec')
])
def test_months_select(page, list_option_value, list_text):
    txt_date = page.locator('#txtDate')
    txt_date.click()
    month_locator = page.locator('.ui-datepicker-month')
    month_locator.select_option(list_option_value)
    assert month_locator.input_value() == list_option_value, f'Selected value is not {list_option_value}'

    selected_month = month_locator.locator('option:checked').text_content()
    assert ''.join(selected_month.split()) == list_text, F'Displayed text is not {list_text}'


@pytest.mark.smoke
@pytest.mark.parametrize('list_option_value, list_text', [
    ('2015', '2015'),
    ('2016', '2016'),
    ('2017', '2017'),
    ('2018', '2018'),
    ('2019', '2019'),
    ('2020', '2020'),
    ('2021', '2021'),
    ('2022', '2022'),
    ('2023', '2023'),
    ('2024', '2024'),
    ('2025', '2025'),
    ('2026', '2026'),
    ('2027', '2027'),
    ('2028', '2028'),
    ('2029', '2029'),
    ('2030', '2030'),
    ('2031', '2031'),
    ('2032', '2032'),
    ('2033', '2033'),
    ('2034', '2034'),
    ('2035', '2035')
])
def test_years_select(page, list_option_value, list_text):
    txt_date = page.locator('#txtDate')
    txt_date.click()
    year_locator = page.locator('.ui-datepicker-year')
    year_locator.select_option(list_option_value)
    assert year_locator.input_value() == list_option_value, f'Selected value is not {list_option_value}'

    selected_year = year_locator.locator('option:checked').text_content()
    assert ''.join(selected_year.split()) == list_text, F'Displayed text is not {list_text}'


@pytest.mark.smoke
def test_full_date(page, test_run_month_day_year_data, test_validation_month_day_year_data):
    txt_date = page.locator('#txtDate')

    current_year = datetime.now().year
    min_year = current_year - 0
    max_year = current_year + 0

    for year, months in test_run_month_day_year_data.items():
        if min_year <= int(year) <= max_year:
            for month, expected_dates in months.items():
                for day in expected_dates:
                    # Reopen the date picker for each date selection
                    txt_date.click()
                    year_locator = page.locator('.ui-datepicker-year')
                    month_locator = page.locator('.ui-datepicker-month')

                    # Select the year and month
                    year_locator.select_option(year)
                    month_locator.select_option(str(helpers_functions.month_name_to_index(month)))

                    # Click the specific date
                    date_locator = page.locator(
                        f".ui-datepicker-calendar td[data-handler='selectDay'] a[data-date='{day}']"
                    )
                    date_locator.click()

                    # Verify the selected date in the text input
                    actual_date_str = txt_date.input_value()

                    # Validate the actual result using validation_month_day_year_data
                    expected_validation_date = test_validation_month_day_year_data[year][month][int(day) - 1]

                    print(f"Validated Date: {actual_date_str} is correct for {expected_validation_date}")
                    assert actual_date_str == expected_validation_date, (
                        f"Date mismatch for {day} {month} {year}. "
                        f"Expected: {expected_validation_date}, Got: {actual_date_str}"
                    )


@pytest.mark.smoke
def test_next_month_year(page, test_run_month_day_year_data):
    txt_date = page.locator('#txtDate')
    txt_date.click()

    # Locate the year and month selectors
    year_locator = page.locator('.ui-datepicker-year')
    month_locator = page.locator('.ui-datepicker-month')

    # Get the starting year and month
    start_year = year_locator.locator('option[selected]').text_content()
    start_moth = month_locator.locator('option[selected]').text_content()

    # Flatten the test data into a list of (year, month) pairs for validation
    expected_dates = [
        (year, month) for year, month in test_run_month_day_year_data.items() for month in month.keys()
    ]

    # Index for keeping track of the expected (year, month) during validation
    index = expected_dates.index((start_year, start_moth))

    for click_next in range(24):
        page.locator('.ui-datepicker-next').click()
        index = (index + 1) % len(expected_dates)
        current_year = year_locator.locator('option[selected]').text_content()
        current_month = month_locator.locator('option[selected]').text_content()

        expected_year, expected_month = expected_dates[index]
        print(f"After clicking next: Current year: {current_year}, Current month: {current_month}")
        assert current_year == expected_year, f"Year mismatch: expected {expected_year}, got {current_year}"
        assert current_month == current_month, f"Month mismatch: expected {expected_month}, got {current_month}"


@pytest.mark.smoke
def test_prev_month_year(page, test_run_month_day_year_data):
    text_date = page.locator('#txtDate')
    text_date.click()

    year_locator = page.locator('.ui-datepicker-year')
    month_locator = page.locator('.ui-datepicker-month')

    # Get the starting year and month
    start_year = year_locator.locator('option[selected]').text_content()
    start_moth = month_locator.locator('option[selected]').text_content()

    # Flatten the test data into a list of (year, month) pairs for validation
    expected_dates = [
        (year, month) for year, month in test_run_month_day_year_data.items() for month in month.keys()
    ]

    # Index for keeping track of the expected (year, month) during validation
    index = expected_dates.index((start_year, start_moth))

    for click_prev in range(24):
        page.locator('.ui-datepicker-prev').click()
        index = (index - 1) % len(expected_dates)
        current_year = year_locator.locator('option[selected]').text_content()
        current_month = month_locator.locator('option[selected]').text_content()

        expected_year, expected_month = expected_dates[index]
        print(f"After clicking previous: Current year: {current_year}, Current month: {current_month}")
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
    text_locator = page.locator('#txtDate')
    text_locator.click()

    day_headers = page.locator('.ui-datepicker-calendar thead th span')

    values_days = [header.get_attribute('title') for header in day_headers.all()]
    assert day_value in values_days, f"Expected short day '{day_value}' not found in {values_days}"

    id_days = [header.text_content() for header in day_headers.all()]
    assert day_id in id_days, f"Expected short day '{day_id}' not found in {id_days}"



