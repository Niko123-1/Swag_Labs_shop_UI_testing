from pages.base_page import BasePage
from playwright.sync_api import Page, expect

class LoginPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        # Локаторы элементов страницы
        self.username_input = page.locator('[data-test="username"]')
        self.password_input = page.locator('[data-test="password"]')
        self.login_button = page.locator('[data-test="login-button"]')
        self.error_alert = page.locator('[data-test="error"]')

    def fill_login_form(self, username: str, password: str):
        """
        Метод для заполнения формы логина
        :param username: юзер
        :param password: пароль
        :return: -
        """
        self.username_input.fill(username)
        expect(self.username_input).to_have_value(username)  # Проверяем, что email введен корректно

        self.password_input.fill(password)
        expect(self.password_input).to_have_value(password)  # Проверяем, что пароль введен корректно

    def click_login_button(self):
        """
        Метод для нажатия на кнопку Login
        :return:
        """
        self.login_button.click()

    def check_username_required_message(self):
        """
        Метод для проверки логина без username
        :return:
        """
        expect(self.error_alert).to_be_visible()
        expect(self.error_alert).to_have_text("Epic sadface: Username is required")

    def check_password_required_message(self):
        """
        Метод для проверки логина без password
        :return:
        """
        expect(self.error_alert).to_be_visible()
        expect(self.error_alert).to_have_text("Epic sadface: Password is required")

    def check_locked_out_user_message(self):
        """
        Метод для проверки логина заблокированного пользователя
        :return:
        """
        expect(self.error_alert).to_be_visible()
        expect(self.error_alert).to_have_text("Epic sadface: Sorry, this user has been locked out.")

    def check_wrong_email_or_password_message(self):
        """
        Метод для проверки логина c невалидными данными
        :return:
        """
        expect(self.error_alert).to_be_visible()
        expect(self.error_alert).to_have_text("Epic sadface: Username and password do not match any user in this service")