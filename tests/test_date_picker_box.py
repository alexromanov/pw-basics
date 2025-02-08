import time
import pytest
from playwright.sync_api import expect
import utils.helpers as helpers_functions
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


@pytest.mark.smoke
def test_hover_date_picker_box(page):
    """
    @brief Verifies that hovering over the date picker box changes its size.
    @param page The Playwright page instance.

    @test
    1. Locate the `.date-picker-box` element.
    2. Retrieve its initial width and height.
    3. Hover over the `.date-picker-box` element.
    4. Capture the width and height after hovering.
    5. Verify that the width and height change upon hovering.

    @assert The width of the `.date-picker-box` should change after hovering.
    @assert The height of the `.date-picker-box` should change after hovering.
    """

    date_picker = page.locator('.date-picker-box')
    date_picker.hover()

    initial_width = date_picker.bounding_box()['width']
    initial_height = date_picker.bounding_box()['height']

    date_picker.hover()

    hover_width = date_picker.bounding_box()['width']
    hover_height = date_picker.bounding_box()['height']

    assert initial_width != hover_width, f"Date picker box width did not change on hover: {hover_width} == {initial_width}"
    assert initial_height != hover_height, f"Date picker box height did not change on hover: {hover_height} == {initial_height}"


@pytest.mark.smoke
def test_hover_submit_button(page):
    """
    @brief Verifies that the background color of the submit button changes when hovered.
    @param page The Playwright page instance.

    @test
    1. Locate the `.submit-btn` element.
    2. Retrieve the initial background color of the submit button.
    3. Hover over the submit button.
    4. Wait for 200ms to allow the hover effect to take place.
    5. Retrieve the background color after hovering.
    6. Compare the initial and hover background colors.

    @assert The background color of the `.submit-btn` should change after hovering.
    """

    submit_button = page.locator('.submit-btn')

    initial_color = submit_button.evaluate("element => window.getComputedStyle(element).getPropertyValue('background-color')")
    submit_button.hover()
    page.wait_for_timeout(200)
    hover_color = submit_button.evaluate("element => window.getComputedStyle(element).getPropertyValue('background-color')")

    assert initial_color != hover_color, (f"Background color did not change on hover. Initial: "
                                          f"{initial_color}, Hover: {hover_color}")


@pytest.mark.smoke
def test_date_from(page, random_dates):
    """
    @brief Verifies that the user can correctly select and submit a date range.
    @param page The Playwright page instance.
    @param random_dates A tuple (start_date, end_date) provided by the fixture.

    @test
    1. Retrieve start and end dates from the fixture.
    2. Locate the start and end date input fields.
    3. Fill in the start and end dates.
    4. Verify that the entered dates match expected values.
    5. Click the submit button.
    6. Capture and verify the displayed result.

    @assert The start and end dates must match the actual input values.
    @assert The displayed date range must match the expected value.
    """

    # Use the fixture-generated dates
    start_date, end_date = random_dates

    # Fill and verify start date
    start_date_input = page.locator('input#start-date')
    start_date_input.fill(start_date)
    actual_start_date = start_date_input.input_value()
    assert start_date == actual_start_date, f"Start date mismatch. Expected: {start_date}, Actual: {actual_start_date}"

    # Fill and verify end date
    end_date_input = page.locator('input#end-date')
    end_date_input.fill(end_date)
    actual_end_date = end_date_input.input_value()
    assert end_date == actual_end_date, f"End date mismatch. Expected: {end_date}, Actual: {actual_end_date}"

    # Submit the form
    submit_button = page.locator('.submit-btn')
    submit_button.click()

    # Verify the result
    result = page.locator('#result')
    result_text = result.text_content()
    selected_days_range = helpers_functions.clean_date_string(result_text)
    actual_days_range = helpers_functions.calculate_date_difference(actual_start_date, actual_end_date)

    assert str(selected_days_range) == str(actual_days_range), f"Days range mismatch. Expected: {actual_days_range}, Actual: {selected_days_range}"


