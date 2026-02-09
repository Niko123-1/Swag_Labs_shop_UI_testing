from random import sample

from pages.base_page import BasePage
from playwright.sync_api import Page, expect
from components.footer.footer_component import FooterComponent
from components.navigation.burger_menu_component import BurgerMenuComponent
from components.navigation.shopping_cart_component import ShoppingCartComponent
from pages.shopping_cart_page import ShoppingCartPage
from tools.faker import fake

class CheckoutInformationPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.checkout_title = page.locator('[data-test="title"]')

        self.checkout_info_first_name = page.locator('[data-test="firstName"]')
        self.checkout_info_last_name = page.locator('[data-test="lastName"]')
        self.checkout_info_postal_code = page.locator('[data-test="postalCode"]')

        self.checkout_continue_button = page.locator('[data-test="continue"]')
        self.checkout_cancel_button = page.locator('[data-test="cancel"]')

        self.checkout_error_message = page.locator('[data-tst="error"]')
        self.checkout_error_message_close_button = page.locator('[data-tst="error-button"]')

        self.footer = FooterComponent(page)
        self.burger_menu = BurgerMenuComponent(page)
        self.shopping_cart = ShoppingCartComponent(page)
        self.non_empty_cart = ShoppingCartPage(page)


    def check_checkout_information_title(self):
        expect(self.checkout_title).to_have_text('Checkout: Your Information')

    def check_checkout_information_form(self):
        expect(self.checkout_info_first_name).to_be_visible()
        expect(self.checkout_info_last_name).to_be_visible()
        expect(self.checkout_info_postal_code).to_be_visible()

    def check_checkout_information_form_fill_in(self, firstname, lastname, postalcode):
        self.checkout_info_first_name.fill(firstname)
        self.checkout_info_last_name.fill(lastname)
        self.checkout_info_postal_code.fill(postalcode)

    def check_checkout_cancel(self):
        self.checkout_cancel_button.click()
        self.non_empty_cart.check_shopping_cart_title()
        self.non_empty_cart.check_shopping_cart_labels()
        self.non_empty_cart.check_shopping_cart_details()

    def check_checkout_continue(self):
        self.check_checkout_information_form_fill_in()
        self.checkout_continue_button.click()
        # add check out review pge



