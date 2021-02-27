import pytest
from selenium import webdriver

text_in_btn_add_to_basket = None

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru, en-gb, es or fr")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    if language == "ru":
        print("\ncheck ru localisation..")
        text_in_btn_add_to_basket = "Добавить в корзину"
    elif language == "es":
        print("\ncheck en-gb localisation..")
        text_in_btn_add_to_basket = "Add to basket"
    elif language == "es":
        print("\ncheck es localisation..")
        text_in_btn_add_to_basket = "Añadir al carrito"
    elif language == "fr":
        print("\ncheck fr localisation..")
        text_in_btn_add_to_basket = "Ajouter au panier"
    else:
        raise pytest.UsageError("--language should be ru, en-gb, es or fr")
    link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207//"
    browser = webdriver.Chrome()
    browser.get(link)
    yield browser
    print("\nquit browser..")
    browser.quit()
