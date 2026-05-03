from playwright.sync_api import Page
from pages.base_page import BasePage


class CheckboxPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.expand_all_button = page.locator(".rc-tree-switcher.rc-tree-switcher_close").first
        self.home_checkbox = page.get_by_label("Select Home")
        self.result = page.locator("#result")

    
    def expand_all(self) -> None:
        self.expand_all_button.click()

    
    def select_home(self) -> None:
        self.home_checkbox.click()