import time

import utils.helpers as helpers_functions


def get_one_page_data_dict(page):
    goods_data_dict = {}

    table = page.locator('#productTable')
    rows = table.locator('tbody tr').all()[1:]

    for row in rows:
        columns = row.locator('td').all_inner_texts()[:-1]
        row_id, name, price = columns
        if row_id not in goods_data_dict:
            goods_data_dict[row_id] = {'name': name, 'price': price}

    return goods_data_dict


def get_pages_num(page):
    pages_nums_list = []

    nums_element = page.locator('#pagination')
    nums_element_list = nums_element.locator('li').all()
    for num in nums_element_list:
        page_num = num.locator('a').all_inner_texts()
        pages_nums_list.extend(page_num)

    return pages_nums_list


def get_all_gages_data_dict(page):
    # pages_nums_list = get_pages_num(page)
    # for page in
    pagination = page.locator("#pagination a")
    for page in range(pagination.count()):
        pagination.nth(page).click()
        time.sleep(2)

    # rows = page.locator("#productTable tbody tr").all()[1:]
    rows = pagination.locator('tbody tr').all()[1:]

    for row in rows:
        columns = row.locator('td').all_inner_texts()[:-1]

def main():
    playwright, browser, context, page = helpers_functions.helpers_get_page()
    get_all_gages_data_dict(page)
    # books_data_dict = collect_data(page)
    browser.close()
    playwright.stop()


if __name__ == '__main__':
    main()
