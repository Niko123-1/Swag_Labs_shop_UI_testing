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

        self.checkout_error_message = page.locator('[data-test="error"]')
        self.checkout_error_message_close_button = page.locator('[data-test="error-button"]')

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

    def fill_checkout_information_form(self, first_name: str, last_name: str, postal_code: str):
        self.checkout_info_first_name.fill(first_name)
        expect(self.checkout_info_first_name).to_have_value(first_name)  # Проверяем, что email введен корректно

        self.checkout_info_last_name.fill(last_name)
        expect(self.checkout_info_last_name).to_have_value(last_name)  # Проверяем, что пароль введен корректно

        self.checkout_info_postal_code.fill(postal_code)
        expect(self.checkout_info_postal_code).to_have_value(postal_code)

    def click_continue_button(self):
        expect(self.checkout_continue_button).to_be_visible()
        self.checkout_continue_button.click()

    def click_cancel_button(self):
        expect(self.checkout_cancel_button).to_be_visible()
        self.checkout_cancel_button.click()

    def check_continue_with_out_required_fields(self, error_message: str):
        self.click_continue_button()
        expect(self.checkout_error_message).to_have_text(error_message)

    def check_successful_checkout_continue(self):
        self.fill_checkout_information_form(first_name=fake.first_name(), last_name=fake.last_name(), postal_code=fake.postal_code())
        self.click_continue_button()
        self.page.wait_for_timeout(2000)



