btn_add_to_basket_locator = ".btn-add-to-basket"

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_check_is_btn_add_to_basket_in_recuired_language(browser, text_in_btn_add_to_basket):
    browser.get(link)

    btn_add_to_basket = browser.find_element_by_css_selector(btn_add_to_basket_locator)

    assert btn_add_to_basket.text == text_in_btn_add_to_basket
    print(btn_add_to_basket.text, text_in_btn_add_to_basket, sep=' = ')

# selenium_env\Scripts\activate.bat
# pytest -s -v --language=ru module_4/part_1/test_items.py
# pytest --language=es module_4\part_1\test_items.py
