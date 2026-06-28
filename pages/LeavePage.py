from pages.BasePage import BasePage
from config.LocatorManager import locator_manager


class LeavePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.leave_link_locator = locator_manager.get_locator("leave_page", "leave_page_link", page)

    def click_on_leave_link(self):
        self.click("leave link", self.leave_link_locator)