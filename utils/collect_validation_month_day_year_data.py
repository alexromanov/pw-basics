import json
from pprint import pprint
import random
from playwright.sync_api import sync_playwright
from datetime import datetime


def collect_validation_month_day_year_data(page):
    """
    @brief Collects all available dates from the date picker for validation.
    @param page The Playwright page instance.
    @return A dictionary containing years as keys, each holding another dictionary
            where months are keys, and the values are lists of available dates in
            "DD/MM/YYYY" format.
    """

    all_dates_dict = {}

    date_input = page.locator('#txtDate')
    date_input.click()

    months = page.locator('.ui-datepicker-month option').all_inner_texts()
    years = page.locator('.ui-datepicker-year option').all_inner_texts()

    for year in years:
        page.locator('.ui-datepicker-year').select_option(year)
        all_dates_dict[year] = {}

        for month_index, month in enumerate(months):
            page.locator('.ui-datepicker-month').select_option(str(month_index))
            dates = page.locator('.ui-datepicker-calendar td[data-handler="selectDay"] a').all_inner_texts()

            actual_dates = [
                f"{str(day).zfill(2)}/{str(month_index + 1).zfill(2)}/{year}" for day in dates
            ]

            all_dates_dict[year][month] = actual_dates

    return all_dates_dict


def save_data_to_file(data, file_name='validation_month_day_year_data.json'):
    """
    @brief Saves collected date validation data into a JSON file.

    @param data The dictionary containing the extracted dates.
    @param file_name The name of the file where the data should be stored.
    """
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)


def main():
    """
    @brief Main function to extract date picker data and save it to a file.

    Steps:
    1. Launch a headless browser using Playwright.
    2. Open a new browser context and page.
    3. Navigate to the test automation practice website.
    4. Extract available dates from the date picker.
    5. Save the extracted data into a JSON file.
    6. Close the browser.
    """

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.goto('https://testautomationpractice.blogspot.com/')
        dates_test_data = collect_validation_month_day_year_data(page)
        save_data_to_file(dates_test_data)
        browser.close()


if __name__ == '__main__':
    main()
