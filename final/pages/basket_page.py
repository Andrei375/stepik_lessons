from final.pages.base_page import BasePage
from final.pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        self.should_not_be_products_in_the_basket()
        self.should_be_text_of_empty_basket()

    def should_not_be_products_in_the_basket(self):
        # Assert
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET_LOCATOR)

    def should_be_text_of_empty_basket(self):
        # Assert
        assert self.is_element_present(*BasketPageLocators.BASKET_MESSAGE_LOCATOR)
