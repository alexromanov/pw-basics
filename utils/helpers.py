import json
from pprint import pprint
import random
from playwright.sync_api import sync_playwright
from datetime import datetime


def month_name_to_index(month_name):
    months = {
        "January": 0, "February": 1, "March": 2, "April": 3, "June": 5,
        "July": 6, "August": 7, "September": 8, "October": 9, "November": 10, "December": 11,
        "Jan": 0, "Feb": 1, "Mar": 2, "Apr": 3, "May": 4, "Jun": 5,
        "Jul": 6, "Aug": 7, "Sep": 8, "Oct": 9, "Nov": 10, "Dec": 11,
    }
    return months[month_name]


def format_date_data(month, date, year):
    original_date = f'{month}/{date}/{year}'
    date_obj = datetime.strptime(original_date, "%b/%d/%Y")
    formatted_date = date_obj.strftime("%m/%d/%Y")

    return formatted_date


def pick_random_date(date_picker_test_data):
    year = random.choice(list(date_picker_test_data.keys()))
    months = date_picker_test_data[year]
    month = random.choice(list(months.keys()))
    dates = months[month]
    date = random.choice(dates)

    return year, month, date


def day_month_format(date_line):
    date_list = date_line.split('/')
    day = date_list[0]
    month = date_list[1]
    year = date_list[2]
    for date in date_list:
        if len(date) == 1:
            return f'0{day}/0{month}/{year}'


def clean_date_string(date_string):
    return date_string.split()[-2]


def generate_start_end_date():
    start_year = random.randint(2020, 2030)
    start_month = random.randint(1, 12)
    is_leap_year = (start_year % 4 == 0 and start_year % 100 != 0) or (start_year % 400 == 0)

    if start_month == 2:
        if is_leap_year:
            day = random.randint(1, 29)
            end_day = random.randint(day, 29)
        else:
            day = random.randint(1, 28)
            end_day = random.randint(day, 28)

    elif start_month in [4, 6, 9, 11]:
        day = random.randint(1, 30)
        end_day = random.randint(day, 30)
    else:
        day = random.randint(1, 31)
        end_day = random.randint(day, 31)

    end_year = random.randint(start_year, 2030)
    end_month = random.randint(start_month, 12)

    start_date = f'{start_year}-{start_month:02d}-{day:02d}'
    end_date = f'{end_year}-{end_month:02d}-{end_day:02d}'

    return str(start_date), str(end_date)


def calculate_date_difference(start_date, end_date):
    """
    Calculate the difference in days between two dates.

    Args:
        start_date (str): The start date in 'YYYY-MM-DD' format.
        end_date (str): The end date in 'YYYY-MM-DD' format.

    Returns:
        int: The difference in days between the two dates.
    """

    start = datetime.strptime(start_date, '%Y-%m-%d')
    end = datetime.strptime(end_date, '%Y-%m-%d')

    difference = abs((start - end).days)

    return difference


def helpers_get_page():
    """
    @brief Initializes Playwright, launches a Chromium browser, and navigates to the test page.
    @return page A Playwright page instance.
    """
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://testautomationpractice.blogspot.com")

    return playwright, browser, context, page
