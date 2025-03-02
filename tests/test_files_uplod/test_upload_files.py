import os
import time
import pytest
import utils.helpers as helpers_functions
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


@pytest.mark.smoke
def test_upload_single_file(page, file_path):
    """
    1. Define the file path to be uploaded.
    2. Locate the file input field.
    3. Upload the file using `set_input_files()`.
    4. Retrieve the actual file name from the input field.
    5. Compare the uploaded file name with the expected file name.
    """

    file_input = page.locator('input#singleFileInput')
    file_input.set_input_files(file_path)

    actual_file_name = file_input.evaluate("element => element.files[0].name")
    expected_file_name = 'Updated_Resume_Sr_Python_Engineer.pdf'

    assert actual_file_name == expected_file_name, f"File upload failed. Expected: {expected_file_name}, Got: {actual_file_name}"


@pytest.mark.smoke
def test_upload_multiple_files(page, file_path):
    """
    1. Locate the multiple file input field.
    2. Set multiple files (two copies of the same file) for upload.
    3. Retrieve the names of the uploaded files.
    4. Click the upload button to submit the files.
    5. Extract the file status displayed after upload.
    6. Verify that both uploaded files are correctly listed in the file status.
    7. Validate that the actual uploaded file names match the expected file name.
    """

    file_input = page.locator('input#multipleFilesInput')
    file_input.set_input_files(file_path)
    file_input.set_input_files([file_path, file_path])

    actual_file_name_one = file_input.evaluate("element => element.files[0].name")
    actual_file_name_two = file_input.evaluate("element => element.files[1].name")

    upload_button = page.locator('button', has_text="Upload Multiple Files")
    upload_button.click()

    file_status = page.locator('#multipleFilesStatus').text_content()

    assert all(file in file_status for file in [actual_file_name_one, actual_file_name_two]), \
        f"Expected files {actual_file_name_one}, {actual_file_name_two} in {file_status}"

    expected_file_name = 'Updated_Resume_Sr_Python_Engineer.pdf'

    assert actual_file_name_one == expected_file_name, \
        f"File upload failed. Expected: {actual_file_name_one}, Got: {expected_file_name}"
    assert actual_file_name_two == expected_file_name, \
        f"File upload failed. Expected: {actual_file_name_two}, Got: {expected_file_name}"
