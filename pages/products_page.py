from pages.base_page import BasePage
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from components.footer.footer_component import FooterComponent
from components.navigation.burger_menu_component import BurgerMenuComponent
from components.navigation.shopping_cart_component import ShoppingCartComponent

class ProductsPage(BasePage):

    default_sort_value = 'Name (A to Z)'

    def __init__(self, page: Page):
        super().__init__(page)

        #page title locator
        self.products_title = page.locator('[data-test="title"]')

        #products sort locator
        self.products_sort = page.locator('[data-test="product-sort-container"]')

        #item locators
        self.item_link = page.locator('[data-test="item-3-img-link"]')
        self.add_to_cart_button = page.locator('[data-test="add-to-cart-test.allthethings()-t-shirt-(red)"]')
        self.remove_from_cart_button = page.locator('[data-test="remove-test.allthethings()-t-shirt-(red)"]')

        self.footer = FooterComponent(page)
        self.burger_menu = BurgerMenuComponent(page)
        self.shopping_cart = ShoppingCartComponent(page)

    def check_shopping_cart_link_visit(self):
        pass
        # add once sopping cart page is implemented!!!

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

    def check_item_image_is_visible(self):
        #expect(self.item_image).to_be_visible()
        #expect(self.item_image_link).to_be_visible()
        pass

    def check_adding_item_to_cart(self):
        self.add_to_cart_button.click()
        expect(self.remove_from_cart_button).to_be_visible()
        self.shopping_cart.check_shopping_cart_badge_is_visible(1)

    def check_removing_item_from_cart(self):
        self.add_to_cart_button.click()
        self.remove_from_cart_button.click()
        expect(self.add_to_cart_button).to_be_visible()
        self.shopping_cart.check_shopping_cart_badge_is_not_visible()




    



