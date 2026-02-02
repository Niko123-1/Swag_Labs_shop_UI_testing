import pytest
from pages.login_page import LoginPage

@pytest.mark.parametrize("username,password", [
    ("", ""),
    ("", "secret_sauce")
])

def test_without_email_login(login_page: LoginPage, username: str, password: str):
    login_page.visit("https://www.saucedemo.com/")
    login_page.fill_login_form(username=username, password=password)
    login_page.click_login_button()
    login_page.check_username_required_message()

def test_without_password_login(login_page: LoginPage):
    login_page.visit("https://www.saucedemo.com/")
    login_page.fill_login_form(username="standard_user",password="")
    login_page.click_login_button()
    login_page.check_password_required_message()

@pytest.mark.parametrize("username,password", [
    ("standard_user", "asdasd"),
    ("asdasdff", "secret_sauce")
])

def test_wrong_username_or_password_login(login_page: LoginPage, username: str, password: str):
    login_page.visit("https://www.saucedemo.com/")
    login_page.fill_login_form(username=username, password=password)
    login_page.click_login_button()
    login_page.check_wrong_email_or_password_message()

def test_locked_user_login(login_page: LoginPage):
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

def test_successful_login(login_page: LoginPage, username: str, password: str):
    login_page.visit("https://www.saucedemo.com/")
    login_page.fill_login_form(username=username, password=password)
    login_page.click_login_button()