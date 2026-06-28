from pages.BasePage import BasePage
from config.LocatorManager import locator_manager


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username_locator = locator_manager.get_locator("login_page", "username", page)
        self.password_locator = locator_manager.get_locator("login_page", "password", page)
        self.login_button_locator = locator_manager.get_locator("login_page", "login_button", page)
        self.dashboard_locator = locator_manager.get_locator("login_page", "dashboard", page)

    def login(self, username, password):
        self.fill("username", self.username_locator, username)
        self.fill("password", self.password_locator, password)
        self.click("login button", self.login_button_locator)

    def verify_login(self):
        self.expect_visible("dashboard", self.dashboard_locator)