from pages.base_page import BasePage
from playwright.sync_api import Page, expect
from components.footer.footer_component import FooterComponent
from components.navigation.burger_menu_component import BurgerMenuComponent
from components.navigation.shopping_cart_component import ShoppingCartComponent
from pages.products_page import ProductsPage
from pages.shopping_cart_page import ShoppingCartPage
from tools.faker import fake

class CheckoutCompletePage(BasePage):

    thanks_text = 'Thank you for your order!'
    about_order_text = 'Your order has been dispatched, and will arrive just as fast as the pony can get there!'

    def __init__(self, page: Page):
        super().__init__(page)

        self.checkout_complete_title = page.locator('[data-test="title"]')
        self.checkout_complete_icon = page.locator('[data-test="pony-express"]')
        self.checkout_complete_thanks_text = page.locator('[data-test="complete-header"]')
        self.checkout_complete_about_order_text = page.locator('[data-test="complete-text"]')

        self.checkout_complete_back_to_home_button = page.locator('[data-test="back-to-products"]')

        self.footer = FooterComponent(page)
        self.burger_menu = BurgerMenuComponent(page)
        self.shopping_cart = ShoppingCartComponent(page)
        self.products = ProductsPage(page)
        self.empty_cart = ShoppingCartPage(page)

    def back_home_button_click(self):
        self.checkout_complete_back_to_home_button.click()
        self.page.wait_for_timeout(2000)
        expect(self.products.products_title).to_be_visible()

