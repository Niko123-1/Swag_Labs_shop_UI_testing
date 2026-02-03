from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from pages.login_page import LoginPage


class BurgerMenuComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        # burger menu locators
        self.burger_menu_open = page.locator('[data-test="open-menu"]')
        self.all_items_link = page.locator('[data-test="inventory-sidebar-link"]')
        self.about_link = page.locator('[data-test="about-sidebar-link"]')
        self.logout_link = page.locator('[data-test="logout-sidebar-link"]')
        self.reset_app_state_link = page.locator('[data-test="reset-sidebar-link"]')
        self.burger_menu_close = page.locator('[data-test="close-menu"]')

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

    def check_burger_menu_about_option(self):
        self.burger_menu_open.click(force=True)
        expect(self.about_link).to_have_attribute("href", "https://saucelabs.com/")

    def check_burger_menu_all_items_option(self):
        self.burger_menu_open.click(force=True)
        expect(self.all_items_link).to_have_attribute("href", "#")

    def check_burger_menu_logout_option(self):
        self.burger_menu_open.click(force=True)
        expect(self.logout_link).to_have_attribute("href", "#")
        self.logout_link.click()

        login_page = LoginPage(self.page)
        expect(login_page.username_input).to_be_visible()
        expect(login_page.password_input).to_be_visible()
        expect(login_page.login_button).to_be_visible()

    def check_burger_menu_reset_app_state_option(self):
        self.burger_menu_open.click(force=True)
        expect(self.reset_app_state_link).to_have_attribute("href", "#")