import pytest
from playwright.sync_api import Page
from pages.products_page import ProductsPage
from pages.login_page import LoginPage
from pages.item_details_page import ItemDetailsPage
from pages.shopping_cart_page import ShoppingCartPage


@pytest.fixture
def page(chromium_page: Page) -> Page:
    """Базовая фикстура страницы с настройками"""
    chromium_page.set_viewport_size({"width": 1920, "height": 1080})
    chromium_page.goto("https://www.saucedemo.com/")
    return chromium_page


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    """Фикстура страницы логина"""
    return LoginPage(page=page)


@pytest.fixture
def logged_in_page(page: Page) -> Page:
    """Фикстура для авторизованной страницы"""
    login_page = LoginPage(page=page)
    login_page.fill_login_form(username='standard_user', password='secret_sauce')
    login_page.click_login_button()
    page.wait_for_url("**/inventory.html")
    return page


@pytest.fixture
def products_page(logged_in_page: Page) -> ProductsPage:
    """Фикстура страницы продуктов"""
    return ProductsPage(page=logged_in_page)


@pytest.fixture
def item_details_page(products_page: ProductsPage, page: Page) -> ItemDetailsPage:
    """Фикстура страницы деталей товара"""
    products_page.item_link.click()
    page.wait_for_url("**/inventory-item.html?id=*")
    return ItemDetailsPage(page=page)


@pytest.fixture
def not_empty_shopping_cart_page(item_details_page: ItemDetailsPage, page: Page) -> ShoppingCartPage:
    """Фикстура страницы корзины"""
    item_details_page.add_to_cart_button.click()
    item_details_page.shopping_cart.shopping_cart_link.click()
    page.wait_for_url("**/cart.html")
    return ShoppingCartPage(page=page)

@pytest.fixture
def empty_shopping_cart_page(item_details_page: ItemDetailsPage, page: Page) -> ShoppingCartPage:
    """Фикстура страницы корзины"""
    item_details_page.shopping_cart.shopping_cart_link.click()
    page.wait_for_url("**/cart.html")
    return ShoppingCartPage(page=page)