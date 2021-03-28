from final.pages.base_page import BasePage
from final.pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # Assert
        assert "login" in self.browser.current_url, \
            "Login page url is not correct"

    def should_be_login_form(self):
        # Assert
        assert self.is_element_present(*LoginPageLocators.INPUT_LOGIN_USERNAME), \
            "Login text input in login form  is not presented"
        assert self.is_element_present(*LoginPageLocators.INPUT_LOGIN_PASSWORD), \
            "Password text input in login form  is not presented"

    def should_be_register_form(self):
        # Assert
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        # Act
        email_field = self.browser.find_element(*LoginPageLocators.INPUT_REGISTRATION_EMAIL)
        password_field = self.browser.find_element(*LoginPageLocators.INPUT_REGISTRATION_PASSWORD_1)
        confirm_password_field = self.browser.find_element(*LoginPageLocators.INPUT_REGISTRATION_PASSWORD_2)
        register_button = self.browser.find_element(*LoginPageLocators.SUBMIT_REGISTRATION_BUTTON)
        email_field.send_keys(email)
        password_field.send_keys(password)
        confirm_password_field.send_keys(password)
        register_button.click()
