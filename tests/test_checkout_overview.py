import allure

from pages.checkout_overview_page import CheckoutOverviewPage
import pytest

@pytest.mark.checkout
class TestCheckoutOverview:

    def test_checkout_finish(self, checkout_overview_page: CheckoutOverviewPage):
        checkout_overview_page.finish_button_click()

    def test_check_burger_menu_interaction(self, checkout_overview_page: CheckoutOverviewPage):
        checkout_overview_page.burger_menu.check_burger_menu_is_visible()
        checkout_overview_page.burger_menu.check_burger_menu_is_opening()
        checkout_overview_page.burger_menu.check_burger_menu_list()
        checkout_overview_page.burger_menu.check_burger_menu_is_closing()

    def test_burger_menu_menu_all_items_option(self, checkout_overview_page: CheckoutOverviewPage):
        checkout_overview_page.burger_menu.check_burger_menu_all_items_option()

    def test_burger_menu_menu_about_option(self, checkout_overview_page: CheckoutOverviewPage):
        checkout_overview_page.burger_menu.check_burger_menu_about_option()

    def test_burger_menu_menu_reset_app_state_option(self, checkout_overview_page: CheckoutOverviewPage):
        checkout_overview_page.burger_menu.check_burger_menu_reset_app_state_option()

    def test_burger_menu_menu_logout_option(self, checkout_overview_page: CheckoutOverviewPage):
        checkout_overview_page.burger_menu.check_burger_menu_logout_option()

    def test_page_footer(self, checkout_overview_page: CheckoutOverviewPage):
        checkout_overview_page.footer.check_footer_info()
        checkout_overview_page.footer.check_twitter_social_link()
        checkout_overview_page.footer.check_linkedin_social_link()
        checkout_overview_page.footer.check_facebook_social_link()