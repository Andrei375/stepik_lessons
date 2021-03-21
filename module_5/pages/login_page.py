from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):  # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, \
            "Login page url is not correct"

    def should_be_login_form(self):  # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.INPUT_LOGIN_USERNAME), \
            "Login text input in login form  is not presented"
        assert self.is_element_present(*LoginPageLocators.INPUT_LOGIN_PASSWORD), \
            "Password text input in login form  is not presented"

    def should_be_register_form(self):  # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.INPUT_REGISTRATION_EMAIL), \
            "Login text input in registration form  is not presented"
        assert self.is_element_present(*LoginPageLocators.INPUT_REGISTRATION_PASSWORD_1), \
            "Password_1 text input in registration form is not presented "
        assert self.is_element_present(*LoginPageLocators.INPUT_REGISTRATION_PASSWORD_2), \
            "Password_2 text input in registration form  is not presented "

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.INPUT_REGISTRATION_EMAIL)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.INPUT_REGISTRATION_PASSWORD_1)
        password_field.send_keys(password)
        confirm_password_field = self.browser.find_element(*LoginPageLocators.INPUT_REGISTRATION_PASSWORD_2)
        confirm_password_field.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.SUBMIT_REGISTRATION_BUTTON)
        register_button.click()
