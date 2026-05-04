import allure
import pytest
from playwright.sync_api import Page, expect
from pages.buttons_page import ButtonsPage


@pytest.mark.smoke
@allure.epic("Web UI")
@allure.title("Двойной клик")
@allure.description("Проверяем двойной клик по кнопке и вывод текста")
@allure.feature("Buttons")
@allure.story("Double click")
@allure.severity(allure.severity_level.NORMAL)
def test_double_click(page: Page) -> None:
    current_page = ButtonsPage(page)

    with allure.step("Открываем страницу с кнопками"):
        current_page.open("https://demoqa.com/buttons")

    with allure.step("Совершаем двойной клик"):
        current_page.double_click()

    with allure.step("Проверяем что вывод о совершённом действии отображён на странице"):
        expect(current_page.double_btn_message).to_be_visible()


@pytest.mark.smoke
@allure.epic("Web UI")
@allure.title("Клик правой кнопкой мыши")
@allure.description("Проверяем клик правой кнопки мыши и вывод текста")
@allure.feature("Buttons")
@allure.story("Right button click")
@allure.severity(allure.severity_level.NORMAL)
def test_right_click(page: Page) -> None:
    current_page = ButtonsPage(page)

    with allure.step("Открываем страницу с кнопками"):
        current_page.open("https://demoqa.com/buttons")

    with allure.step("Совершаем клик правой кнопкой мыши"):
        current_page.right_click()

    with allure.step("Проверяем что вывод о совершённом действии отображён на странице"):
        expect(current_page.right_btn_message).to_be_visible()


@pytest.mark.smoke
@allure.epic("Web UI")  
@allure.title("Стандартный клик")
@allure.description("Проверяем клик левой кнопки мыши и вывод текста")
@allure.feature("Buttons")
@allure.story("Left button click")
@allure.severity(allure.severity_level.NORMAL)
def test_click(page: Page) -> None:
    current_page = ButtonsPage(page)

    with allure.step("Открываем страницу с кнопками"):
        current_page.open("https://demoqa.com/buttons")

    with allure.step("Совершаем клик левой кнопкой мыши"):
        current_page.click()

    with allure.step("Проверяем что вывод о совершённом действии отображён на странице"):
        expect(current_page.normal_btn_message).to_be_visible()
