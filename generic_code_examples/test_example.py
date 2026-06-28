def test_login(page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Uses default timeout (30 sec)
    page.locator("input[name='username']").fill("Admin")

    # Override timeout only for this action
    page.locator("input[name='password']").fill("admin123", timeout=10000)

    # Override timeout only for this click
    page.locator("button[type='submit']").click(timeout=15000)

    # Wait for URL
    page.wait_for_url("**/dashboard", timeout=20000)