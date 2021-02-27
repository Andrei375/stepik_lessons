import pytest
from selenium import webdriver

from module_4.part_1.conftest import text_in_btn_add_to_basket

btn_add_to_basket_locator = ".btn-add-to-basket"


@pytest.mark.parametrize()
def test_check_is_btn_add_to_basket_in_recuired_language(browser):
    btn_add_to_basket = browser.find_element_by_css_selector(btn_add_to_basket_locator)

    assert btn_add_to_basket.text == text_in_btn_add_to_basket

# pytest -s -v --language=ru part_1/test_items.py
