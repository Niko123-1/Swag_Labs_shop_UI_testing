import pytest
from pages.products_page import ProductsPage

def test_check_burger_menu_interaction(products_page: ProductsPage):
    products_page.check_burger_menu_is_visible()
    products_page.check_burger_menu_is_opening()
    products_page.check_burger_menu_list()
    products_page.check_burger_menu_is_closing()

def test_shopping_cart_interaction(products_page: ProductsPage):
    products_page.check_shopping_cart_badge_is_not_visible()
    products_page.check_shopping_cart_link_is_visible()
    products_page.check_shopping_cart_link_visit()

def test_products_page_title_displaying(products_page: ProductsPage):
    products_page.check_title_is_visible()


def test_product_sort_dropdown_list_visible(products_page: ProductsPage):
    products_page.check_products_sorting_dropdown_list_visible()

@pytest.mark.parametrize("value", ["Name (Z to A)", "Price (low to high)", "Price (high to low)", "Name (A to Z)"])
def test_product_sort_dropdown_list_interaction(products_page: ProductsPage, value: str):
    products_page.check_selection_of_value_from_products_sorting_dropdown_list(value)

