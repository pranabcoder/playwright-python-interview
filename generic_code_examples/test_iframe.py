import time


def test_iframe(page):
    page.goto('https://testing.qaautomationlabs.com/iframe.php')
    frame = page.frame_locator("[name='iframe1']").locator("form.p-4:visible")
    frame.get_by_role("button").click()
    time.sleep(5)