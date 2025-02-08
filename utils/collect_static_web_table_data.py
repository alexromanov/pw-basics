import json
from pprint import pprint
from playwright.sync_api import sync_playwright
import utils.helpers as helpers_functions


def collect_data(page):
    books_data_dict = {}

    table = page.locator('table[name="BookTable"]')
    rows = table.locator('tbody tr').all()[1:]

    for row in rows:
        columns = row.locator('td').all_inner_texts()
        book_name, author, subject, price = columns
        if subject not in books_data_dict:
            books_data_dict[subject] = {}

        if author not in books_data_dict[subject]:
            books_data_dict[subject][author] = {}

        books_data_dict[subject][author][book_name] = {'Price': price}

    return books_data_dict


def save_data_to_file(data, file_name='static_web_table_test_data.json'):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)


def main():
    playwright, browser, context, page = helpers_functions.helpers_get_page()
    books_data_dict = collect_data(page)
    # save_data_to_file(books_data_dict)
    browser.close()
    playwright.stop()


if __name__ == '__main__':
    main()
