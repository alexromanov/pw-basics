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
