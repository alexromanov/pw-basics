# Tasks
1. Check current project structure
2. Init new repo and push it to your GH
3. Add requirements.txt and put all dependencies inside
4. Add virtual environment to the project (venv)
5. Add .gitignore and ignore all files from venv
6. Implement all tests from test_practice.py (with different types of locators)
7. Add markers to tests (smoke, regression, etc)
8. Move all additional functions to utils/helpers.py
9. Add GH action to run tests on the CRON job - once a day (optional)
10. Add GH action to run tests manually (optional, for next time)
11. Add reporting to the GH action (ctrf, Allure, Extent Report) (really optional, for next time)

# How to run tests
* Install all dependencies: pytest, pytest-playwright, pytest-xdist, pytest-dotenv
* Install browsers: `playwright install`
* Run tests: `pytest`