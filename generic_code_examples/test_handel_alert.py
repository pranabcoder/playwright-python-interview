import time


def test_handel_alert(page):
    page.goto("https://demoqa.com/alerts")
    page.on("dialog", lambda dialog: (
        print(dialog.message),
        dialog.accept()
    ))
    page.locator("#alertButton").click()
    time.sleep(5)

