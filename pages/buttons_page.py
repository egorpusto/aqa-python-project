from playwright.sync_api import Page
from pages.base_page import BasePage


class ButtonsPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.double_btn = page.locator("#doubleClickBtn")
        self.double_btn_message = page.locator("#doubleClickMessage")
        self.right_btn = page.locator("#rightClickBtn")
        self.right_btn_message = page.locator("#rightClickMessage")
        self.normal_btn = page.get_by_role("button", name="Click Me").last
        self.normal_btn_message = page.locator("#dynamicClickMessage")


    def double_click(self) -> None:
        self.double_btn.dblclick()
    

    def right_click(self) -> None:
        self.right_btn.click(button='right')
    

    def click(self) -> None:
        self.normal_btn.click()