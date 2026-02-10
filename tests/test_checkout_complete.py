from tools.faker import fake

from pages.checkout_complete_page import CheckoutCompletePage
import pytest

class TestCheckoutComplete:

    def test_check_burger_menu_interaction(self, checkout_complete_page: CheckoutCompletePage):
        checkout_complete_page.burger_menu.check_burger_menu_is_visible()
        checkout_complete_page.burger_menu.check_burger_menu_is_opening()
        checkout_complete_page.burger_menu.check_burger_menu_list()
        checkout_complete_page.burger_menu.check_burger_menu_is_closing()

    def test_burger_menu_menu_all_items_option(self, checkout_complete_page: CheckoutCompletePage):
        checkout_complete_page.burger_menu.check_burger_menu_all_items_option()

    def test_burger_menu_menu_about_option(self, checkout_complete_page: CheckoutCompletePage):
        checkout_complete_page.burger_menu.check_burger_menu_about_option()

    def test_burger_menu_menu_reset_app_state_option(self, checkout_complete_page: CheckoutCompletePage):
        checkout_complete_page.burger_menu.check_burger_menu_reset_app_state_option()

    def test_burger_menu_menu_logout_option(self, checkout_complete_page: CheckoutCompletePage):
        checkout_complete_page.burger_menu.check_burger_menu_logout_option()

    def test_page_footer(self, checkout_complete_page: CheckoutCompletePage):
        checkout_complete_page.footer.check_footer_info()
        checkout_complete_page.footer.check_twitter_social_link()
        checkout_complete_page.footer.check_linkedin_social_link()
        checkout_complete_page.footer.check_facebook_social_link()

    def test_back_home_button(self, checkout_complete_page: CheckoutCompletePage):
        checkout_complete_page.back_home_button_click()