from pprint import pprint

import pytest
import utils.helpers as helpers_functions
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


@pytest.mark.smoke
def test_static_web_table(page, web_table_test_data):
    """
    @brief Verifies that the static web table contains the expected book data.

    @param page The Playwright page instance.
    @param web_table_test_data The expected book data stored in a structured dictionary format.

    @test
    1. Extract the expected table data from the test dataset (`web_table_test_data`).
    2. Locate the table element using its `name` attribute.
    3. Retrieve all table rows, excluding the header.
    4. Extract actual data from the table by iterating through rows and collecting cell values.
    5. Compare the extracted table data (`actual_rows_data_list`) with expected data (`expected_rows_data_list`).
    6. Identify any missing or unexpected rows in the table.

    @assert The actual table rows should match the expected rows.
    @assert There should be no missing rows in the table.
    @assert There should be no unexpected extra rows in the table.
    """
    expected_rows_data_list = []
    for subject, value_dict in web_table_test_data.items():
        for author, author_dict in value_dict.items():
            for book_name, book_name_dict in author_dict.items():
                price = str(book_name_dict.get("Price"))
                expected_rows_data_list.append([book_name, author, subject, price])

    table = page.locator('table[name=BookTable]')
    rows = table.locator('tbody tr').all()[1:]

    actual_rows_data_list = []
    for row in rows:
        row_list = [cell for cell in row.locator('td').all_inner_texts()]
        actual_rows_data_list.append(row_list)

    missing_rows = [row for row in expected_rows_data_list if row not in actual_rows_data_list]
    unexpected_rows = [row for row in actual_rows_data_list if row not in expected_rows_data_list]

    assert not missing_rows, f"❌ Missing rows in the table: {missing_rows}"
    assert not unexpected_rows, f"❌ Unexpected extra rows found in the table: {unexpected_rows}"
