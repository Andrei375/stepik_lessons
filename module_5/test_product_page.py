from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
import pytest
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"


class TestProductPage:
    @pytest.mark.parametrize('promo_offer',
                             ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6",
                              pytest.param("offer7", marks=pytest.mark.xfail),
                              "offer8", "offer9"])
    def test_guest_can_add_product_to_basket(self, browser, promo_offer):
        product_link = f"{link}/?promo={promo_offer}"
        page = ProductPage(browser, product_link)
        page.open()

        page.add_to_basket()
        page.solve_quiz_and_get_code()

        page.should_be_correct_product_in_basket()

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()

        page.add_to_basket()

        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()

        page.should_not_be_success_message()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        page = ProductPage(browser, link)
        page.open()

        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)

        basket_page.should_be_empty_basket()


@pytest.mark.login_user
class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@wrongmail.org"
        password = "Qwaszx@123"

        page = LoginPage(browser, link)
        page.open()

        page.go_to_login_page()
        page.register_new_user(email, password)

        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()

        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()

        page.add_to_basket()

        page.should_be_correct_product_in_basket()

# selenium_env\Scripts\activate.bat
# pytest -s module_5\test_product_page.py
