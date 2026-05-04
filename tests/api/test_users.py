import allure
import pytest
from utils.api_client import ApiClient


@pytest.mark.smoke
@allure.title("Получение списка пользователей")
@allure.description("Проверяем что GET /api/users возвращает 200")
@allure.feature("Users")
@allure.severity(allure.severity_level.NORMAL)
def test_get_user(api_client: ApiClient) -> None:
    with allure.step("Отправляем GET запрос"):
        response = api_client.get("/api/users")

    with allure.step("Проверяем статус код"):
        assert response.status_code == 200


@pytest.mark.regress
@allure.title("Получение единственного пользователя")
@allure.description("Проверяем что GET /api/users/2 возвращает 200")
@allure.feature("Users")
@allure.severity(allure.severity_level.NORMAL)
def test_get_single_user(api_client: ApiClient) -> None:
    with allure.step("Отправляем GET запрос"):
        response = api_client.get("/api/users/2")

    with allure.step("Проверяем статус код"):
        assert response.status_code == 200

    with allure.step("Проверяем id полученного пользователя"):
        assert response.json()["data"]["id"] == 2


@pytest.mark.regress
@allure.title("Получение пользователя на второй странице")
@allure.description("Проверяем что GET /api/users?page=2 возвращает 200")
@allure.feature("Users")
@allure.severity(allure.severity_level.NORMAL)
def test_get_users_page_2(api_client: ApiClient) -> None:
    with allure.step("Отправляем GET запрос"):
        response = api_client.get("/api/users?page=2")

    with allure.step("Проверяем статус код"):
        assert response.status_code == 200


@pytest.mark.regress
@allure.title("Получение несуществующего пользователя")
@allure.description("Проверяем что GET /api/users/999 возвращает 404")
@allure.feature("Users")
@allure.severity(allure.severity_level.NORMAL)
def test_get_nonexistent_user(api_client: ApiClient) -> None:
    with allure.step("Отправляем GET запрос"):
        response = api_client.get("/api/users/999")

    with allure.step("Проверяем статус код"):
        assert response.status_code == 404


@pytest.mark.smoke
@allure.title("Создание пользователя")
@allure.description("Проверяем что POST /api/users возвращает 201")
@allure.feature("Users")
@allure.severity(allure.severity_level.NORMAL)
def test_create_user(api_client: ApiClient) -> None:
    with allure.step("Отправляем POST запрос"):
        response = api_client.post(
            "/api/users",
            {"name": "John", "job": "QA"}
        )

    with allure.step("Проверяем статус код"):
        assert response.status_code == 201


@pytest.mark.smoke
@allure.title("Создание пользователя и проверка его имени в ответе")
@allure.description("Проверяем что POST /api/users возвращает json c именем пользователя")
@allure.feature("Users")
@allure.severity(allure.severity_level.NORMAL)
def test_create_user_check_name(api_client: ApiClient) -> None:
    with allure.step("Отправляем POST запрос"):
        response = api_client.post(
            "/api/users",
            {"name": "Bob", "job": "HR"}
        )
    
    with allure.step("Проверяем статус код"):
        assert response.status_code == 201

    with allure.step("Проверяем имя пользователя в ответе"):
        assert response.json()["name"] == "Bob"


@pytest.mark.smoke
@allure.title("Обновление данных пользователя")
@allure.description("Проверяем что POST /api/users/2 возвращает 200")
@allure.feature("Users")
@allure.severity(allure.severity_level.NORMAL)
def test_update_user(api_client: ApiClient) -> None:
    with allure.step("Отправляем PUT запрос"):
        response = api_client.put(
            "/api/users/2",
            {"name": "Mike", "job": "Developer"}
        )

    with allure.step("Проверяем статус код"):
        assert response.status_code == 200

@pytest.mark.regress
@allure.title("Удаление пользователя")
@allure.description("Проверяем что DELETE /api/users/2 возвращает 204")
@allure.feature("Users")
@allure.severity(allure.severity_level.NORMAL)
def test_delete_user(api_client: ApiClient) -> None:
    with allure.step("Отправляем DELETE запрос"):
        response = api_client.delete("/api/users/2")

    with allure.step("Проверяем статус код"):
        assert response.status_code == 204