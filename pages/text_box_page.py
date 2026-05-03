from playwright.sync_api import Page
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.full_name = page.locator("#userName")
        self.email = page.locator("#userEmail")
        self.current_address = page.locator("#currentAddress")
        self.permanent_address = page.locator("#permanentAddress")
        self.submit_button = page.locator("#submit")
        self.output = page.locator("#output")


    def fill_form(
            self, 
            name: str, 
            email: str, 
            current_address: str, 
            permanent_address: str
        ) -> None:
        
        self.full_name.fill(name)
        self.email.fill(email)
        self.current_address.fill(current_address)
        self.permanent_address.fill(permanent_address)


    def submit(self) -> None:
        self.submit_button.click()