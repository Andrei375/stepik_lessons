import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru, en-gb, es or fr")


@pytest.fixture(scope="function")
def text_in_btn_add_to_basket(request):
    language = request.config.getoption("language")
    if language == "ru":
        print("\ncheck ru localisation..")
        return "Добавить в корзину"
    elif language == "en-gb":
        print("\ncheck en-gb localisation..")
        return "Add to basket"
    elif language == "es":
        print("\ncheck es localisation..")
        return "Añadir al carrito"
    elif language == "fr":
        print("\ncheck fr localisation..")
        return "Ajouter au panier"


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    if language == "ru":
        print("\ncheck ru localisation..")
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    elif language == "en-gb":
        print("\ncheck en-gb localisation..")
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    elif language == "es":
        print("\ncheck es localisation..")
        link = "http://selenium1py.pythonanywhere.com/es/catalogue/coders-at-work_207/"
    elif language == "fr":
        print("\ncheck fr localisation..")
        link = "http://selenium1py.pythonanywhere.com/fr/catalogue/coders-at-work_207/"
    else:
        raise pytest.UsageError("--language should be ru, en-gb, es or fr")
    browser = webdriver.Chrome()
    browser.get(link)  # в test_items.py не видно link, поэтому оставил здесь
    yield browser
    print("\nquit browser..")
    browser.quit()
