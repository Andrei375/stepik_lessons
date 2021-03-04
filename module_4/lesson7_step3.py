import time
import math
import pytest
from selenium import webdriver


def answer():
    return str(math.log(int(time.time())))


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    # browser.quit()


@pytest.mark.parametrize('part_link', ["895", "896", "897", "898", "899", "903", "904", "905"])
def test_insert_answer(browser, part_link):
    link = f"https://stepik.org/lesson/236{part_link}/step/1"
    browser.get(link)

    browser.find_element_by_css_selector(".textarea").send_keys(answer())
    browser.find_element_by_css_selector(".submit-submission").click()

    assert "Correct!", browser.find_element_by_css_selector("")

# selenium_env\Scripts\activate.bat
# pytest lesson7_step3.py
