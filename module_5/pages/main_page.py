from selenium.webdriver.common.by import By
from .base_page import BasePage


class MainPage(BasePage):
    def go_to_login_page(self):
        link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        link.click()

    def should_be_login_link(self):
        self.browser.find_element(By.CSS_SELECTOR, "#login_link"), "Login link is not presented"
