from playwright.sync_api import expect
import allure


class BasePage:
    def __init__(self, page):
        self.page = page

    def open(self, url):
        with allure.step(f"Open page: {url}"):
            self.page.goto(url)

    def click(self, name, locator):
        with allure.step(f"Click: {name}"):
            locator.click()

    def fill(self, name, locator, value):
        with allure.step(f"Fill: {name}"):
            locator.fill(value)

    def text(self, name, locator):
        with allure.step(f"Read text: {name}"):
            return locator.text_content()

    def is_visible(self, name, locator):
        with allure.step(f"Check visible: {name}"):
            return locator.is_visible()

    def expect_visible(self, name, locator):
        with allure.step(f"Expect visible: {name}"):
            expect(locator).to_be_visible()