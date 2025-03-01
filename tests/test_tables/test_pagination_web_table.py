import pytest
import logging


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


@pytest.mark.smoke
def test_static_web_table(page, pagination_pages_data_dict):
    for key, value in pagination_pages_data_dict.items():
        print(key, value)