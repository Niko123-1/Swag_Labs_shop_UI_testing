import allure

from pages.checkout_complete_page import CheckoutCompletePage
import pytest

@pytest.mark.checkout
class TestCheckoutComplete:

    @allure.title('Check interaction with burger menu: open and close')
    def test_check_burger_menu_interaction(self, checkout_complete_page: CheckoutCompletePage):
        checkout_complete_page.burger_menu.check_burger_menu_is_visible()
        checkout_complete_page.burger_menu.check_burger_menu_is_opening()
        checkout_complete_page.burger_menu.check_burger_menu_list()
        checkout_complete_page.burger_menu.check_burger_menu_is_closing()

    @allure.title('Check "All Items" in burger menu')
    def test_burger_menu_all_items_option(self, checkout_complete_page: CheckoutCompletePage):
        checkout_complete_page.burger_menu.check_burger_menu_all_items_option()

    @allure.title('Check "About" in burger menu')
    def test_burger_menu_about_option(self, checkout_complete_page: CheckoutCompletePage):
        checkout_complete_page.burger_menu.check_burger_menu_about_option()

    @allure.title('Check "Reset App" in burger menu')
    def test_burger_menu_reset_app_state_option(self, checkout_complete_page: CheckoutCompletePage):
        checkout_complete_page.burger_menu.check_burger_menu_reset_app_state_option()

    @allure.title('Check "Logout" in burger menu')
    def test_burger_menu_logout_option(self, checkout_complete_page: CheckoutCompletePage):
        checkout_complete_page.burger_menu.check_burger_menu_logout_option()

    @allure.title('Check footer: copy info, twitter, linkedin, facebook social media links')
    def test_page_footer(self, checkout_complete_page: CheckoutCompletePage):
        checkout_complete_page.footer.check_footer_info()
        checkout_complete_page.footer.check_twitter_social_link()
        checkout_complete_page.footer.check_linkedin_social_link()
        checkout_complete_page.footer.check_facebook_social_link()

    @allure.title('Check back to home after order completion')
    def test_back_home_button(self, checkout_complete_page: CheckoutCompletePage):
        checkout_complete_page.back_home_button_click()