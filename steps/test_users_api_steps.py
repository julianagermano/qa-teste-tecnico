import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from jsonschema import validate
from schemas.users_schema import LIST_SCHEMA

scenarios("../features/users_api.feature")

@pytest.fixture
def context():
    return {}

@given("que a API reqres.in está disponível")
def api_available(api_request_context):
    assert api_request_context is not None

@when("eu solicito a lista de usuários na página 2")
def request_page_2(api_request_context, context):
    response = api_request_context.get("users", params={"page": "2"})
    context["response"] = response
    context["body"] = response.json()

@then("o status da resposta deve ser 200")
def check_status(context):
    assert context["response"].status == 200

@then("a resposta deve conter exatamente 6 usuários")
def check_count(context):
    assert len(context["body"]["data"]) == 6

@then("cada usuário deve conter os campos obrigatórios")
def check_schema(context):
    validate(instance=context["body"], schema=LIST_SCHEMA)

@then(parsers.parse('o campo "page" da resposta deve ser igual a {value:d}'))
def check_page_field(context, value):
    assert context["body"]["page"] == value