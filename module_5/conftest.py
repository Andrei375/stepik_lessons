import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en-GB',
                     help="Choose language: ru, en-gb, es or fr")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    options = Options()
    if language == "ru":
        print("\ncheck ru localisation..")
        options.add_experimental_option('prefs', {'intl.accept_languages': 'ru'})
    elif language == "en-GB":
        print("\ncheck en-GB localisation..")
        options.add_experimental_option('prefs', {'intl.accept_languages': 'en-GB'})
    elif language == "es":
        print("\ncheck es localisation..")
        options.add_experimental_option('prefs', {'intl.accept_languages': 'es'})
    elif language == "fr":
        print("\ncheck fr localisation..")
        options.add_experimental_option('prefs', {'intl.accept_languages': 'fr'})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
