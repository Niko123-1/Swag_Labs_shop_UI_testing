import pytest
from playwright.sync_api import Page
from pages.products_page import ProductsPage
from pages.login_page import LoginPage


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