import time

import pytest

from pages.LeavePage import LeavePage

@pytest.mark.smoke
def test_leave_page_functionality(logged_in_application):
    leave_page = LeavePage(logged_in_application)
    leave_page.click_on_leave_link()
    time.sleep(5)