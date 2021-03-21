from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    INPUT_LOGIN_USERNAME = (By.CSS_SELECTOR, "#id_login-username")
    INPUT_LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")

    INPUT_REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    INPUT_REGISTRATION_PASSWORD_1 = (By.CSS_SELECTOR, "#id_registration-password1")
    INPUT_REGISTRATION_PASSWORD_2 = (By.CSS_SELECTOR, "#id_registration-password2")
    SUBMIT_REGISTRATION_BUTTON = (By.CSS_SELECTOR, "[name = 'registration_submit']")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    CORRECT_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages > div:nth-child(1) strong")
    CORRECT_PRODUCT_PRICE = (By.CSS_SELECTOR, ".alertinner > p > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-of-type(1) .alertinner")


class BasketPageLocators:
    BASKET_MESSAGE_LOCATOR = (By.CSS_SELECTOR, "#content_inner p")
    PRODUCT_IN_BASKET_LOCATOR = (By.CSS_SELECTOR, ".basket-items")
