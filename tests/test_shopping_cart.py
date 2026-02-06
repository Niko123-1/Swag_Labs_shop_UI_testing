import pytest
from pages.shopping_cart_page import ShoppingCartPage

def test_check_burger_menu_interaction(shopping_cart_page: ShoppingCartPage):
    shopping_cart_page.burger_menu.check_burger_menu_is_visible()
    shopping_cart_page.burger_menu.check_burger_menu_is_opening()
    shopping_cart_page.burger_menu.check_burger_menu_list()
    shopping_cart_page.burger_menu.check_burger_menu_is_closing()