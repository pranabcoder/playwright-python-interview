import pytest
from playwright.sync_api import sync_playwright
import allure
from config.framework_config import config
from pages.LoginPage import LoginPage


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = getattr(p, config.browser).launch(headless=config.headless)
        yield browser
        browser.close()


@pytest.fixture()
def page(browser):
    context = browser.new_context(
        base_url=config.base_url,
        viewport=config.viewport,
        record_video_dir="videos/"
    )

    if config.trace != "off":
        context.tracing.start(screenshots=True, snapshots=True)

    page = context.new_page()
    yield page

    if config.trace != "off":
        context.tracing.stop(path="traces/trace.zip")
    context.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed and "page" in item.funcargs:
        page = item.funcargs["page"]
        allure.attach(
            page.screenshot(type="png"),
            name="failure_screenshot",
            attachment_type=allure.attachment_type.PNG
        )
        allure.attach(
            page.content(),
            name="page_source",
            attachment_type=allure.attachment_type.HTML
        )


@pytest.fixture()
def logged_in_application(page):
    login = LoginPage(page)
    login.open(config.base_url)
    login.login("Admin", "admin123")
    login.verify_login()
    return page
