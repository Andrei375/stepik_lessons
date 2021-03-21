from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()

    def should_be_correct_product_in_basket(self):
        self.should_be_correct_product_name()
        self.should_be_correct_product_price()

    def should_be_correct_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        correct_product_name = self.browser.find_element(*ProductPageLocators.CORRECT_PRODUCT_NAME).text

        assert product_name == correct_product_name, "Product name is not correct"

    def should_be_correct_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        correct_product_price = self.browser.find_element(*ProductPageLocators.CORRECT_PRODUCT_PRICE).text

        assert product_price == correct_product_price, "Product price is not correct"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message presents, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message appears, but should not be"
