from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        self.should_not_be_products_in_basket()
        self.should_be_the_text_about_empty_basket()

    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET_LOCATOR)

    def should_be_the_text_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_MESSAGE_LOCATOR)
