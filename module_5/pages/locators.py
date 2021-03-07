from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    INPUT_LOGIN_USERNAME = (By.CSS_SELECTOR, "#id_login-username")
    INPUT_LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")

    INPUT_REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    INPUT_REGISTRATION_PASSWORD_1 = (By.CSS_SELECTOR, "#id_registration-password1")
    INPUT_REGISTRATION_PASSWORD_2 = (By.CSS_SELECTOR, "#id_registration-password2")
