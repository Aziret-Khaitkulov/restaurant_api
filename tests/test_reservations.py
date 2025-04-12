from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_reservations():
    # Отправляем запрос на получение бронирований
    response = client.get("/reservations/")
    # Проверим, что ответ имеет статус 200 OK
    assert response.status_code == 200
    # Проверим, что ответ - это список
    assert isinstance(response.json(), list)
