import time
from pathlib import Path

def test_image_upload(page):
    page.goto("https://www.remove.bg/upload")

    with page.expect_file_chooser() as fc_info:
        page.get_by_role("button", name="Upload Image").click()

    file_chooser = fc_info.value
    image_path = Path(__file__).parent / "images" / "testing.jpeg"
    file_chooser.set_files(str(image_path))
    time.sleep(5)