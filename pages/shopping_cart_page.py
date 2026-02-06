from pages.base_page import BasePage
from playwright.sync_api import Page, expect
from components.footer.footer_component import FooterComponent
from components.navigation.burger_menu_component import BurgerMenuComponent
from components.navigation.shopping_cart_component import ShoppingCartComponent
import re

from pages.products_page import ProductsPage


class ShoppingCartPage(BasePage):

    item_description = ('This classic Sauce Labs t-shirt is perfect to wear when cozying up to your '
                        'keyboard to automate a few tests. Super-soft and comfy ringspun combed cotton.')

    def __init__(self, page: Page):
        super().__init__(page)

        self.shopping_cart_title = page.locator('[data-test="title"]')
        self.shopping_cart_quantity_label = page.locator('[data-test="cart-quantity-label"]')
        self.shopping_cart_desc_label = page.locator('[data-test="cart-desc-label"]')
        self.shopping_cart_item_quantity = page.locator('[data-test="item-quantity"]')
        self.shopping_cart_item_name = page.locator('[data-test="inventory-item-name"]')
        self.shopping_cart_item_desc = page.locator('[data-test="inventory-item-desc"]')
        self.shopping_cart_item_price = page.locator('[data-test="inventory-item-price"]')
        self.shopping_cart_remove_button = page.locator('[data-test="remove-test.allthethings()-t-shirt-(red)"]')
        self.shopping_cart_continue_shopping_button = page.locator('[data-test="continue-shopping"]')
        self.shopping_cart_checkout_button = page.locator('[data-test="checkout"]')

        self.footer = FooterComponent(page)
        self.burger_menu = BurgerMenuComponent(page)
        self.shopping_cart = ShoppingCartComponent(page)
        self.products_page = ProductsPage(page)

    def check_shopping_cart_title(self):
        expect(self.shopping_cart_title).to_be_visible()
        expect(self.shopping_cart_title).to_have_text('Your Cart')

    def check_shopping_cart_labels(self):
        expect(self.shopping_cart_quantity_label).to_be_visible()
        expect(self.shopping_cart_desc_label).to_be_visible()
        expect(self.shopping_cart_quantity_label).to_have_text('QTY')
        expect(self.shopping_cart_desc_label).to_have_text('Description')

    def check_cart_details(self):
        expect(self.shopping_cart_item_quantity).to_have_text('1')
        expect(self.shopping_cart_item_name).to_have_text('Test.allTheThings() T-Shirt (Red)')
        expect(self.shopping_cart_item_desc).to_have_text(self.item_description)
        pattern = r'^\$\d+\.\d{2}$'
        expect(self.shopping_cart_item_price).to_have_text(re.compile(pattern))

    def check_continue_shopping_action(self):
        self.shopping_cart_continue_shopping_button.click()
        expect(self.products_page.products_title).to_be_visible()
        expect(self.shopping_cart.shopping_cart_badge).to_have_text('1')
        expect(self.products_page.remove_from_cart_button).to_be_visible()

    def check_checkout_action(self):
        pass
        # will be released once check-out page is described

    def check_remove_item_from_cart(self):
        expect(self.shopping_cart_remove_button).to_be_visible()
        self.shopping_cart_remove_button.click()
        self.shopping_cart.check_shopping_cart_badge_is_not_visible()
        expect(self.shopping_cart_item_price).not_to_be_visible()
