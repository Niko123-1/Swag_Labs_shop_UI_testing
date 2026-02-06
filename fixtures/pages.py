import pytest
from playwright.sync_api import Page
from pages.products_page import ProductsPage
from pages.login_page import LoginPage
from pages.item_details_page import ItemDetailsPage
from pages.shopping_cart_page import ShoppingCartPage


@pytest.fixture
def login_page(chromium_page: Page) -> LoginPage:
    return LoginPage(page=chromium_page)


@pytest.fixture
def products_page(chromium_page: Page) -> ProductsPage:
    # Переходим на страницу логина
    chromium_page.goto("https://www.saucedemo.com/")

    # Выполняем логин
    login_page = LoginPage(page=chromium_page)
    login_page.fill_login_form(username='standard_user', password='secret_sauce')
    login_page.click_login_button()

    # Ждем перехода на страницу продуктов
    chromium_page.wait_for_url("**/inventory.html")

    return ProductsPage(page=chromium_page)

@pytest.fixture
def item_details_page(chromium_page: Page) -> ItemDetailsPage:
    # Переходим на страницу логина
    chromium_page.goto("https://www.saucedemo.com/")

    # Выполняем логин
    login_page = LoginPage(page=chromium_page)
    login_page.fill_login_form(username='standard_user', password='secret_sauce')
    login_page.click_login_button()

    chromium_page.wait_for_url("**/inventory.html")

    products_page = ProductsPage(page=chromium_page)
    products_page.item_link.click()

    chromium_page.wait_for_url("**/inventory-item.html?id=3")

    return ItemDetailsPage(page=chromium_page)

@pytest.fixture
def shopping_cart_page(chromium_page: Page) -> ShoppingCartPage:
    # Переходим на страницу логина
    chromium_page.goto("https://www.saucedemo.com/")

    # Выполняем логин
    login_page = LoginPage(page=chromium_page)
    login_page.fill_login_form(username='standard_user', password='secret_sauce')
    login_page.click_login_button()

    chromium_page.wait_for_url("**/inventory.html")

    products_page = ProductsPage(page=chromium_page)
    products_page.item_link.click()

    chromium_page.wait_for_url("**/inventory-item.html?id=3")

    item_details_page = ItemDetailsPage(page=chromium_page)
    item_details_page.add_to_cart_button.click()
    item_details_page.shopping_cart.shopping_cart_link.click()

    chromium_page.wait_for_url("**/cart.html")

    return ShoppingCartPage(page=chromium_page)