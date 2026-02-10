import pytest
from pages.shopping_cart_page import ShoppingCartPage

@pytest.mark.shoppingcart
class TestShoppingCart:

    def test_check_burger_menu_interaction(self, not_empty_shopping_cart_page: ShoppingCartPage):
        not_empty_shopping_cart_page.burger_menu.check_burger_menu_is_visible()
        not_empty_shopping_cart_page.burger_menu.check_burger_menu_is_opening()
        not_empty_shopping_cart_page.burger_menu.check_burger_menu_list()
        not_empty_shopping_cart_page.burger_menu.check_burger_menu_is_closing()

    def test_burger_menu_menu_all_items_option(self, not_empty_shopping_cart_page: ShoppingCartPage):
        not_empty_shopping_cart_page.burger_menu.check_burger_menu_all_items_option()

    def test_burger_menu_menu_about_option(self, not_empty_shopping_cart_page: ShoppingCartPage):
        not_empty_shopping_cart_page.burger_menu.check_burger_menu_about_option()

    def test_burger_menu_menu_reset_app_state_option(self, not_empty_shopping_cart_page: ShoppingCartPage):
        not_empty_shopping_cart_page.burger_menu.check_burger_menu_reset_app_state_option()

    def test_burger_menu_menu_logout_option(self, not_empty_shopping_cart_page: ShoppingCartPage):
        not_empty_shopping_cart_page.burger_menu.check_burger_menu_logout_option()

    def test_page_footer(self, not_empty_shopping_cart_page: ShoppingCartPage):
        not_empty_shopping_cart_page.footer.check_footer_info()
        not_empty_shopping_cart_page.footer.check_twitter_social_link()
        not_empty_shopping_cart_page.footer.check_linkedin_social_link()
        not_empty_shopping_cart_page.footer.check_facebook_social_link()

    def test_empty_shopping_cart(self, empty_shopping_cart_page: ShoppingCartPage):
        empty_shopping_cart_page.check_empty_shopping_cart()

    def test_not_empty_shopping_cart_details(self, not_empty_shopping_cart_page: ShoppingCartPage):
        not_empty_shopping_cart_page.check_shopping_cart_details()

    def test_remove_from_shopping_cart(self, not_empty_shopping_cart_page: ShoppingCartPage):
        not_empty_shopping_cart_page.check_remove_item_from_cart()

    def test_continue_shopping(self, not_empty_shopping_cart_page: ShoppingCartPage):
        not_empty_shopping_cart_page.check_continue_shopping_action()

    def test_checkout(self):
        pass
        # add once check-out page delivered