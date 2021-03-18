from pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


class TestProductPage:
    def test_guest_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)  # инициализируем Page Object
        page.open()  # открываем страницу
        page.add_to_basket()
        page.solve_quiz_and_get_code()

# selenium_env\Scripts\activate.bat
# pytest -s module_5\test_product_page.py
