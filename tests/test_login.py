import pytest
import allure
from pages.login_page import LoginPage

@pytest.mark.authorization
class TestLogin:

    @pytest.mark.parametrize("username,password", [
        ("", ""),
        ("", "secret_sauce")
    ])
    @allure.title('Attempt to login w/o email')
    def test_without_email_login(self, login_page: LoginPage, username: str, password: str):
        login_page.visit("https://www.saucedemo.com/")
        login_page.fill_login_form(username=username, password=password)
        login_page.click_login_button()
        login_page.check_username_required_message()

    @allure.title('Attempt to login w/o password')
    def test_without_password_login(self, login_page: LoginPage):
        login_page.visit("https://www.saucedemo.com/")
        login_page.fill_login_form(username="standard_user",password="")
        login_page.click_login_button()
        login_page.check_password_required_message()

    @pytest.mark.parametrize("username,password", [
        ("standard_user", "asdasd"),
        ("asdasdff", "secret_sauce")
    ])
    @allure.title('Attempt to login with wrong email/password')
    def test_wrong_username_or_password_login(self, login_page: LoginPage, username: str, password: str):
        login_page.visit("https://www.saucedemo.com/")
        login_page.fill_login_form(username=username, password=password)
        login_page.click_login_button()
        login_page.check_wrong_email_or_password_message()

    @allure.title('Login with locked user')
    def test_locked_user_login(self, login_page: LoginPage):
        login_page.visit("https://www.saucedemo.com/")
        login_page.fill_login_form(username='locked_out_user', password='secret_sauce')
        login_page.click_login_button()
        login_page.check_locked_out_user_message()

    @pytest.mark.parametrize("username,password", [
        ("standard_user", "secret_sauce"),
        ("problem_user", "secret_sauce"),
        ("performance_glitch_user", "secret_sauce"),
        ("error_user", "secret_sauce"),
        ("visual_user", "secret_sauce"),
    ])

    @allure.title('Login with valid email/password')
    def test_successful_login(self, login_page: LoginPage, username: str, password: str):
        login_page.visit("https://www.saucedemo.com/")
        login_page.fill_login_form(username=username, password=password)
        login_page.click_login_button()