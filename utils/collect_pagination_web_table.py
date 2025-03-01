import utils.helpers as helpers_functions


def get_all_pages_data_dict(page):
    """
    @brief Extracts product table data from all paginated pages.
    @param page The Playwright page instance.

    @description
    This function iterates through each pagination page and extracts product details from
    the displayed table. The extracted data is structured and returned as a dictionary.

    @usage
    - Navigate through each pagination link.
    - Extract all rows of product data from each page.
    - Store the extracted data using page numbers as dictionary keys.

    @return A dictionary containing product details from all pages, structured as:
    ```json
    {
        "1": [{"num_id": "6", "name": "Bluetooth Speaker", "price": "$9.99"}, ...],
        "2": [{"num_id": "11", "name": "Smart Home Hub", "price": "$20.99"}, ...],
        ...
    }
    ```
    """
    all_pages_data_dict = {}

    # Locate pagination links and count total pages
    pagination_links = page.locator("#pagination a")
    total_pages = pagination_links.count()

    for i in range(total_pages):
        page_list = []

        # Re-locate pagination links (as DOM may refresh after each click)
        pagination_links = page.locator("#pagination a")
        page_number = pagination_links.nth(i).text_content()

        # Click on the current pagination link and wait for page load
        pagination_links.nth(i).click()
        page.wait_for_load_state("networkidle")

        # Extract table data from the current page
        table_rows = page.locator("#productTable tbody tr").all()
        for row in table_rows:
            num_id, name, price = row.locator("td").all_inner_texts()[:-1]
            page_list.append({'num_id': num_id,
                              'name': name,
                              'price': price
                              })

        # Store data using page number as the key
        all_pages_data_dict[page_number] = page_list

    return all_pages_data_dict


def main():
    playwright, browser, context, page = helpers_functions.helpers_get_page()
    all_pages_data_dict = get_all_pages_data_dict(page)
    helpers_functions.save_data_to_file(all_pages_data_dict, '../tests/test_tables/pagination_pages_data_dict.json')
    browser.close()
    playwright.stop()


if __name__ == '__main__':
    main()
