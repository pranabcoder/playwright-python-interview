import time


def test_hover_over(page):
    page.goto('https://practice-automation.com/hover/')
    page.locator('#mouse_over').hover()
    time.sleep(5)