import pytest
import logging


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


@pytest.mark.smoke
def test_static_web_table(page, read_file):
    pagination_web_table_validation_data = read_file('pagination_web_table_validation_data.json')

    for key, value in pagination_web_table_validation_data.items():
        print(key, value)