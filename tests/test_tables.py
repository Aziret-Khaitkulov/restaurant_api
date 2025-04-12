from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_get_tables():
    # Отправляем запрос на получение столиков
    response = client.get("/tables")
    # Проверим, что ответ имеет статус 200 OK
    assert response.status_code == 200
    # Проверим, что ответ - это список
    assert isinstance(response.json(), list)
