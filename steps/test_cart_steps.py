import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

scenarios("../features/cart.feature")

@pytest.fixture
def context():
    return {}

@given("que o usuário está logado no SauceDemo")
def login(page, context):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")
    context["inventory"] = InventoryPage(page)
    context["page"] = page

@when(parsers.parse('ele adiciona a "{item}" ao carrinho'))
def add_item(context, item):
    slug = item.lower().replace(" ", "-")
    context["inventory"].add_item(slug)

@then(parsers.parse("o ícone do carrinho deve mostrar {count:d} item"))
def check_badge(context, count):
    expect(context["inventory"].cart_badge).to_have_text(str(count))

@then(parsers.parse('o item "{item}" deve aparecer no carrinho com nome e preço corretos'))
def check_cart_item(context, item):
    context["inventory"].go_to_cart()
    page = context["page"]
    expect(page.locator(".inventory_item_name")).to_have_text(item)
    expect(page.locator(".inventory_item_price")).to_be_visible()