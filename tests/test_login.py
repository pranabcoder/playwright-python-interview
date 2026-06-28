from pages.LoginPage import LoginPage
from config.framework_config import config


def test_login(page):
    login = LoginPage(page)

    login.open(config.base_url)

    login.login("Admin", "admin123")

    return page
