from pages.base_page import BasePage
from playwright.sync_api import Page, expect
from components.footer.footer_component import FooterComponent
from components.navigation.burger_menu_component import BurgerMenuComponent
from components.navigation.shopping_cart_component import ShoppingCartComponent
from pages.products_page import ProductsPage
from pages.shopping_cart_page import ShoppingCartPage
from tools.faker import fake

class CheckoutOverviewPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.checkout_overview_title = page.locator('[data-test="title"]')
        self.checkout_overview_quantity_label = page.locator('[data-test="cart-quantity-label"]')
        self.checkout_overview_desc_label = page.locator('[data-test="cart-desc-label"]')
        self.checkout_overview_item_quantity = page.locator('[data-test="item-quantity"]')
        self.checkout_overview_item_name = page.locator('[data-test="inventory-item-name"]')
        self.checkout_overview_item_desc = page.locator('[data-test="inventory-item-desc"]')
        self.checkout_overview_item_price = page.locator('[data-test="inventory-item-price"]')

        self.checkout_overview_payment_info_label = page.locator('[data-test="payment-info-label"]')
        self.checkout_overview_payment_info_value = page.locator('[data-test="payment-info-value"]')

        self.checkout_overview_shipping_info_label = page.locator('[data-test="shipping-info-label"]')
        self.checkout_overview_shipping_info_value = page.locator('[data-test="shipping-info-value"]')

        self.checkout_overview_total_info_label = page.locator('[data-test="total-info-label"]')
        self.checkout_overview_subtotal_label = page.locator('[data-test="subtotal-label"]')
        self.checkout_overview_tax_label = page.locator('[data-test="tax-label"]')
        self.checkout_overview_summary_total_label = page.locator('[data-test="total-label"]')

        self.checkout_finish_button = page.locator('[data-test="finish"]')
        self.checkout_cancel_button = page.locator('[data-test="cancel"]')

        self.footer = FooterComponent(page)
        self.burger_menu = BurgerMenuComponent(page)
        self.shopping_cart = ShoppingCartComponent(page)
        self.products = ProductsPage(page)
        self.non_empty_cart = ShoppingCartPage(page)

    def finish_button_click(self):
        self.checkout_finish_button.click()

