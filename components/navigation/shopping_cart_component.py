from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class ShoppingCartComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        #shopping cart locators
        self.shopping_cart_link = page.locator('[data-test="shopping-cart-link"]')
        self.shopping_cart_badge = page.locator('[data-test="shopping-cart-badge"]')

    def check_shopping_cart_link_is_visible(self):
        expect(self.shopping_cart_link).to_be_visible()

    def check_shopping_cart_badge_is_visible(self, count: int):
        expect(self.shopping_cart_badge).to_be_visible()
        expect(self.shopping_cart_badge).to_have_text(f"{count}")

    def check_shopping_cart_badge_is_not_visible(self):
        expect(self.shopping_cart_badge).not_to_be_visible()