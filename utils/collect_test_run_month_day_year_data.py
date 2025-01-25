import json
from pprint import pprint
import random
from playwright.sync_api import sync_playwright
from datetime import datetime


def collect_test_run_month_day_year_data(page):
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
            # actual_dates = []
            for day in dates:
                formatted_date = f"{str(month_index + 1).zfill(2)}/{day.zfill(2)}/{year}"
                # actual_dates.append(formatted_date)

                all_dates_dict[year][month] = dates

    return all_dates_dict


def save_data_to_file(data, file_name='test_run_month_day_year_data.json'):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)


def main():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.goto('https://testautomationpractice.blogspot.com/')
        dates_test_data = collect_test_run_month_day_year_data(page)
        save_data_to_file(dates_test_data)
        browser.close()


if __name__ == '__main__':
    main()
