from components.navigation.burger_menu_component import BurgerMenuComponent
from components.navigation.shopping_cart_component import ShoppingCartComponent
from pages.base_page import BasePage
from playwright.sync_api import Page, expect
import re
from pages.products_page import ProductsPage
from components.footer.footer_component import FooterComponent


class ItemDetailsPage(BasePage):

    item_description = ('This classic Sauce Labs t-shirt is perfect to wear when cozying up to '
                        'your keyboard to automate a few tests. '
                        'Super-soft and comfy ringspun combed cotton.')

    def __init__(self, page: Page):
        super().__init__(page)

        # item locators
        self.item_name = page.locator('[data-test="inventory-item-name"]')
        self.item_desc = page.locator('[data-test="inventory-item-desc"]')
        self.item_price = page.locator('[data-test="inventory-item-price"]')
        self.add_to_cart_button = page.locator('[data-test="add-to-cart"]')
        self.remove_from_cart_button = page.locator('[data-test="remove"]')
        self.back_to_products_link = page.locator('[data-test="back-to-products"]')

        self.footer = FooterComponent(page)
        self.burger_menu = BurgerMenuComponent(page)
        self.shopping_cart = ShoppingCartComponent(page)

    def check_item_name(self):
        expect(self.item_name).to_have_text('Test.allTheThings() T-Shirt (Red)')

    def check_item_desc(self):
        expect(self.item_desc).to_have_text(self.item_description)

    def check_price_format(self):
        pattern = r'^\$\d+\.\d{2}$'
        expect(self.item_price).to_have_text(re.compile(pattern))

    def check_adding_item_to_cart(self):
        self.add_to_cart_button.click()
        expect(self.remove_from_cart_button).to_be_visible()
        expect(self.shopping_cart.check_shopping_cart_badge_is_visible(1))

    def check_removing_item_from_cart(self):
        self.add_to_cart_button.click()
        self.remove_from_cart_button.click()
        expect(self.add_to_cart_button).to_be_visible()
        expect(self.shopping_cart.check_shopping_cart_badge_is_not_visible())

    def check_back_to_products_link(self):
        expect(self.back_to_products_link).to_be_visible()
        self.back_to_products_link.click()
        products_page = ProductsPage(self.page)
        expect(products_page.products_title).to_be_visible()
        expect(products_page.shopping_cart.shopping_cart_link).to_be_visible()
        expect(products_page.products_sort).to_be_visible()


