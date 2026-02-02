import pytest
from pages.products_page import ProductsPage

def test_check_burger_menu_interaction(products_page : ProductsPage):
    products_page.check_burger_menu_is_visible()
    products_page.check_burger_menu_is_opening()
    products_page.check_burger_menu_list()
    products_page.check_burger_menu_is_closing()

def test_shopping_cart_interaction(products_page : ProductsPage):
    products_page.check_shopping_cart_badge_is_not_visible()
    products_page.check_shopping_cart_link_is_visible()
    products_page.check_shopping_cart_link_visit()
