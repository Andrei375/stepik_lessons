from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)  # инициализируем Page Object
        page.open()  # открываем страницу

        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url) # выполняем метод страницы - переходим на страницу логина

        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()

        page.should_be_login_link()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        page = MainPage(browser, link)
        page.open()

        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)

        basket_page.should_be_empty_basket()

# selenium_env\Scripts\activate.bat
# pytest -v --tb=line --language=en-GB module_5\test_main_page.py
# pytest --language=en-GB --alluredir=module_5\allure_result module_5
# allure generate -c -o module_5\allure_report module_5\allure_result
