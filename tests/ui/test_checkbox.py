import allure
import pytest
from playwright.sync_api import Page, expect
from pages.checkbox_page import CheckboxPage

@pytest.mark.smoke
@allure.epic("Web UI")    
@allure.title("Checkboxes")
@allure.description("Выбор чекбокса домашней страницы")
@allure.feature("Checkboxes")
@allure.story("Select checkbox")
@allure.severity(allure.severity_level.NORMAL)
def test_select_home(page: Page) -> None:
    select_page = CheckboxPage(page)

    with allure.step("Открываем страницу с чекбоксами"):
        select_page.open("https://demoqa.com/checkbox")
    
    with allure.step("Открываем все чекбоксы"):
        select_page.expand_all()

    with allure.step("Выбираем первый чекбокс"):
        select_page.select_home()

    with allure.step("Проверяем что информация о выборе отображается на странице"):
        expect(select_page.result).to_be_visible()