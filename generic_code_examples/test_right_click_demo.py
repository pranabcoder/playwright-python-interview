import time


def test_right_click_demo(page):
    page.goto("https://vinothqaacademy.com/mouse-event/")
    page.get_by_role("button", name="Right Click Me").click(button="right")
    time.sleep(5)