import allure
import pytest
from playwright.sync_api import Page, expect
from pages.text_box_page import TextBoxPage

@pytest.mark.smoke
@allure.title("Заполнение формы данными пользователя")
@allure.description("Проверяем что данные вводятся и выводятся на странице")
@allure.feature("Filling")
@allure.severity(allure.severity_level.NORMAL)
def test_fill_form(page: Page) -> None:
    text_page = TextBoxPage(page)

    with allure.step("Открываем страницу с формой"):
        text_page.open("https://demoqa.com/text-box")

    with allure.step("Заполняем форму данными"):
        text_page.fill_form(
            "John Parker",
            "john_parker@email.com",
            "green st., London",
            "red st., Germany"
        )
    with allure.step("Подтверждаем заполнение нажатием кнопки"):
        text_page.submit()

    with allure.step("Проверяем что данные удачно заполнились и видны на странице"):
        expect(text_page.output).to_be_visible()