from pages.base_page import BasePage
from playwright.sync_api import Page, expect

class ProductsPage(BasePage):

    default_sort_value = 'Name (A to Z)'

    def __init__(self, page: Page):
        super().__init__(page)

        #burger menu locators
        self.burger_menu_open = page.locator('[data-test="open-menu"]')
        self.all_items_link = page.locator('[data-test="inventory-sidebar-link"]')
        self.about_link = page.locator('[data-test="about-sidebar-link"]')
        self.logout_link = page.locator('[data-test="logout-sidebar-link"]')
        self.reset_app_state_link = page.locator('[data-test="reset-sidebar-link"]')
        self.burger_menu_close = page.locator('[data-test="close-menu"]')

        #shopping cart locators
        self.shopping_cart_link = page.locator('[data-test="shopping-cart-link"]')
        self.shopping_cart_badge = page.locator('[data-test="shopping-cart-badge"]')

        #page title locator
        self.products_title = page.locator('[data-test="title"]')

        #products sort locator
        self.products_sort = page.locator('[data-test="product-sort-container"]')

        #item locators
        self.item_image = page.locator('[data-test=inventory-"item-sauce-labs-backpack-img"]')
        self.item_name = page.locator('[data-test="inventory-item-name"]')
        self.item_desc = page.locator('[data-test="inventory-item-desc"]')
        self.item_price = page.locator('[data-test="inventory-item-price"]')
        self.add_to_cart_button = page.locator('[data-test="add-to-cart-sauce-labs-backpack"]')
        self.remove_from_cart_button = page.locator('[data-test="remove-sauce-labs-backpack"]')

    def check_burger_menu_is_visible(self):
        expect(self.burger_menu_open).to_be_visible()

    def check_burger_menu_is_opening(self):
        self.burger_menu_open.click(force=True)
        expect(self.burger_menu_close).to_be_visible()

    def check_burger_menu_list(self):
        self.burger_menu_open.click(force=True)

        items = [
            (self.all_items_link, "All Items"),
            (self.about_link, "About"),
            (self.logout_link, "Logout"),
            (self.reset_app_state_link, "Reset App State")
        ]

        for locator, expected_text in items:
            expect(locator).to_be_visible()
            expect(locator).to_contain_text(expected_text)

    def check_burger_menu_is_closing(self):
        self.burger_menu_open.click(force=True)
        self.page.wait_for_timeout(2000)
        self.burger_menu_close.click(force=True)
        expect(self.burger_menu_open).to_be_visible()

    def check_shopping_cart_link_is_visible(self):
        expect(self.shopping_cart_link).to_be_visible()

    def check_shopping_cart_link_visit(self):
        pass

    def check_shopping_cart_badge_is_visible(self, count: int):
        expect(self.shopping_cart_badge).to_be_visible()
        expect(self.shopping_cart_badge).to_have_text(f"{count}")

    def check_shopping_cart_badge_is_not_visible(self):
        expect(self.shopping_cart_badge).not_to_be_visible()

    def check_title_is_visible(self):
        expect(self.products_title).to_be_visible()
        expect(self.products_title).to_have_text('Products')

    def check_products_sorting_dropdown_list_visible(self):
        expect(self.products_sort).to_be_visible()
        expect(self.products_sort).to_contain_text(self.default_sort_value)
        self.products_sort.click()
        self.page.wait_for_timeout(2000)
        expect(self.products_sort.locator("option")).to_contain_text(["Name (A to Z)", "Name (Z to A)", "Price (low to high)", "Price (high to low)"])

    def check_selection_of_value_from_products_sorting_dropdown_list(self, value):
        self.products_sort.select_option(value=value)
        self.page.wait_for_timeout(2000)
        expect(self.products_sort).to_contain_text(value)


