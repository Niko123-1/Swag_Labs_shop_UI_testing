from tools.faker import fake

from pages.checkout_information_page import CheckoutInformationPage
import pytest

class TestCheckoutInformation:

    def test_checkout_information_form(self, checkout_information_page: CheckoutInformationPage):
        checkout_information_page.check_checkout_information_form()

    def test_checkout_continue(self, checkout_information_page: CheckoutInformationPage):
        checkout_information_page.click_continue_button()

    def test_checkout_cancel(self, checkout_information_page: CheckoutInformationPage):
        checkout_information_page.click_cancel_button()

    def test_check_burger_menu_interaction(self, checkout_information_page: CheckoutInformationPage):
        checkout_information_page.burger_menu.check_burger_menu_is_visible()
        checkout_information_page.burger_menu.check_burger_menu_is_opening()
        checkout_information_page.burger_menu.check_burger_menu_list()
        checkout_information_page.burger_menu.check_burger_menu_is_closing()

    def test_burger_menu_menu_all_items_option(self, checkout_information_page: CheckoutInformationPage):
        checkout_information_page.burger_menu.check_burger_menu_all_items_option()

    def test_burger_menu_menu_about_option(self, checkout_information_page: CheckoutInformationPage):
        checkout_information_page.burger_menu.check_burger_menu_about_option()

    def test_burger_menu_menu_reset_app_state_option(self, checkout_information_page: CheckoutInformationPage):
        checkout_information_page.burger_menu.check_burger_menu_reset_app_state_option()

    def test_burger_menu_menu_logout_option(self, checkout_information_page: CheckoutInformationPage):
        checkout_information_page.burger_menu.check_burger_menu_logout_option()

    def test_page_footer(self, checkout_information_page: CheckoutInformationPage):
        checkout_information_page.footer.check_footer_info()
        checkout_information_page.footer.check_twitter_social_link()
        checkout_information_page.footer.check_linkedin_social_link()
        checkout_information_page.footer.check_facebook_social_link()

    @pytest.mark.parametrize("first_name, last_name, postal_code, error_message",
                             [("", "", "", "Error: First Name is required"),
                              (fake.first_name(), "","","Error: Last Name is required"),
                              (fake.first_name(), fake.last_name(), "", "Error: Postal Code is required")])
    def test_checkout_continue_with_out_required_info(self, checkout_information_page: CheckoutInformationPage, first_name, last_name, postal_code, error_message):
        checkout_information_page.fill_checkout_information_form(first_name=first_name,last_name=last_name,postal_code=postal_code)
        checkout_information_page.check_continue_with_out_required_fields(error_message)

    def test_checkout_successful_continue(self, checkout_information_page: CheckoutInformationPage):
        checkout_information_page.check_successful_checkout_continue()
        # add once checkout review page is delivered
