import allure
import pytest
from utils.api_client import ApiClient


@pytest.mark.smoke
@allure.epic("API")   
@allure.title('Авторизация с корректными учетными данными')
@allure.description("Проверяем что POST возвращает 200 и token")
@allure.feature("Auth")
@allure.story("Successful login")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_success(api_client: ApiClient) -> None:
    with allure.step("Отправляем POST запрос"):
        response = api_client.post(
            "/api/login",
            {
                "email": "eve.holt@reqres.in",
                "password": "cityslicka"
            }
        )

    with allure.step("Проверяем статус код"):
        assert response.status_code == 200

    with allure.step("Проверяем что запрос вернул токен"):
        assert "token" in response.json()


@pytest.mark.smoke
@allure.epic("API")
@allure.title("Авторизация с недействительными учетными данными")
@allure.description("Проверяем что POST возвращает 400 и error")
@allure.feature("Auth")
@allure.story("Wrong password login")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_wrong_password(api_client: ApiClient) -> None:
    with allure.step("Отправляем POST запрос"):
        response = api_client.post(
            "/api/login",
            {
                "email": "wrong",
                "password": "cityslicka"
            }
        )

    with allure.step("Проверяем статус код"):
        assert response.status_code == 400

    with allure.step("Проверяем что запрос вернул ошибку"):
        assert "error" in response.json()


@pytest.mark.smoke
@allure.epic("API")
@allure.title("Регистрация с неведённым паролем")
@allure.description("Проверяем что POST возвращает 400")
@allure.feature("Register")
@allure.story("Missing password register")
@allure.severity(allure.severity_level.NORMAL)
def test_register_missing_password(api_client: ApiClient) -> None:
    with allure.step("Отправляем POST запрос"):
        response = api_client.post(
            "/api/register",
            {
                "email": "eve.holt@reqres.in",
            }
        )

    with allure.step("Проверяем статус код"):
        assert response.status_code == 400


@pytest.mark.smoke
@allure.epic("API")
@allure.title("Успешная регистрация")
@allure.description("Проверяем что POST возвращает 200")
@allure.feature("Register")
@allure.story("Successful register")
@allure.severity(allure.severity_level.NORMAL)
def test_register_success(api_client: ApiClient) -> None:
    with allure.step("Отправляем POST запрос"):
        response = api_client.post(
            "/api/register",
            {
                "email": "eve.holt@reqres.in",
                "password": "123123"
            }
        )

    with allure.step("Проверяем статус код"):
        assert response.status_code == 200

    with allure.step("Проверяем что запрос вернул токен"):
        assert "token" in response.json()