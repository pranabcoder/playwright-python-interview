import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Default timeout for all actions
        page.set_default_timeout(30000)

        # Default timeout for navigation
        page.set_default_navigation_timeout(60000)

        yield page

        browser.close()
