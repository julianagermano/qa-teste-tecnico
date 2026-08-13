import time
import pytest
from jsonschema import validate
from schemas.users_schema import LIST_SCHEMA


@pytest.mark.parametrize("page", [1, 2])
def test_get_users_status_and_schema(api_request_context, page):
    response = api_request_context.get("users", params={"page": str(page)})
    assert response.status == 200
    body = response.json()
    validate(instance=body, schema=LIST_SCHEMA)
    assert body["page"] == page


def test_get_users_response_time(api_request_context):
    # 3 amostras, uso a mediana pra reduzir flakiness de rede pública
    durations = []
    for _ in range(3):
        start = time.perf_counter()
        api_request_context.get("users", params={"page": "2"})
        durations.append(time.perf_counter() - start)
    durations.sort()
    median = durations[1]
    assert median < 2.0, f"Tempo de resposta mediano alto: {median:.2f}s"


def test_get_users_nonexistent_page_returns_empty(api_request_context):
    response = api_request_context.get("users", params={"page": "999"})
    assert response.status == 200
    assert response.json()["data"] == []