import pytest
import time
from final.pages.main_page import MainPage
from final.pages.login_page import LoginPage
from final.pages.basket_page import BasketPage

link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        # Arrange
        page = MainPage(browser, link)
        page.open()
        # Act
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        # Assert
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        # Arrange
        page = MainPage(browser, link)
        page.open()
        # Assert
        page.should_be_login_link()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        # Arrange
        page = MainPage(browser, link)
        page.open()
        # Act
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        # Assert
        basket_page.should_be_empty_basket()


@pytest.mark.personal_tests
class TestInputFromMainPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # Data
        email = str(time.time()) + "@tut.by"
        password = "iXXeu22DPA4jv9Z"
        # Arrange
        page = LoginPage(browser, link)
        page.open()
        # Act
        page.go_to_login_page()
        page.register_new_user(email, password)
        # Assert
        page.should_be_authorized_user()

    def test_user_can_open_account_page(self, browser):
        # Arrange
        page = MainPage(browser, link)
        page.open()
        # Act
        page.go_to_account_page()
        # Assert
        page.should_be_account_page()

    @pytest.mark.xfail
    def test_register_new_user(self, browser):
        # Data
        email = str(time.time()) + "@tut.by"
        password = "iXXeu22DPA4jv9Z"
        # Act
        page = LoginPage(browser, link)
        page.open()
        # Assert
        page.should_be_register_form()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    @pytest.mark.xfail
    def test_negative_register_new_user(self, browser):
        # Data
        email = str(time.time()) + "@tut.by"
        password = "0iXXeu22DPA4jv9Z"
        repeat_user_password = "0iXXeu22DPA4jv9Z"
        # Act
        page = LoginPage(browser, link)
        page.open()
        # Assert
        page.should_be_register_form()

    @pytest.mark.xfail
    def test_user_login(self, browser):
        # Data
        email = "kosmos09@tut.by"
        password = "0iXXeu22DPA4jv9Z"
        # Act
        page = LoginPage(browser, link)
        page.open()
        # Assert
        page.should_be_login_form()
        page.should_be_authorized_user()


# selenium_env\Scripts\activate.bat
# pytest --browser_name=chrome --language=en-GB final
# pytest --language=en-GB --alluredir=final\allure_result final
# allure generate -c -o final\allure_report final\allure_result
