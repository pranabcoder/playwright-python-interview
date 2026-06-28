from dataclasses import dataclass


@dataclass
class Config:
    browser = "chromium"
    headless = False
    base_url = "https://opensource-demo.orangehrmlive.com"
    timeout = 30000

    viewport = {
        "width": 1920,
        "height": 1080
    }

    screenshot = "only-on-failure"
    video = "retain-on-failure"
    trace = "retain-on-failure"

    allure_results_dir = "allure-results"
    allure_report_dir = "allure-report"
    screenshot_dir = "screenshots"
    video_dir = "videos"
    trace_dir = "traces"


config = Config()
