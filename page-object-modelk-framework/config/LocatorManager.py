import json
import os


class LocatorManager:
    def __init__(self):
        config_dir = os.path.dirname(__file__)
        locator_file = os.path.join(config_dir, "locator.json")

        with open(locator_file, "r") as f:
            self.locators = json.load(f)

    def get_locator(self, page_name, element_name, page):
        locator_data = self.locators[page_name][element_name]
        locator_type = locator_data["type"]
        value = locator_data["value"]

        if locator_type == "get_by_role":
            role = value["role"]
            options = {k: v for k, v in value.items() if k != "role"}
            return page.get_by_role(role, **options)

        if locator_type == "get_by_placeholder":
            return page.get_by_placeholder(value)

        if locator_type == "get_by_label":
            return page.get_by_label(value)

        if locator_type == "get_by_text":
            return page.get_by_text(value, **locator_data.get("options", {}))

        if locator_type == "locator":
            return page.locator(value)

        raise ValueError(f"Unsupported locator type: {locator_type}")


locator_manager = LocatorManager()
