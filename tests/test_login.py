import pytest
from pages.LoginPage import LoginPage
from config.framework_config import config

@pytest.mark.smoke
def test_login(page):
    login = LoginPage(page)

    login.open(config.base_url)

    login.login("Admin", "admin123")
    login.verify_login()
