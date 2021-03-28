import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en-GB", help="Choose language: ru, en-GB, es, fr")
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture
def language(request):
    return request.config.getoption("--language")


@pytest.fixture
def language(request):
    return request.config.getoption("language")


@pytest.fixture(scope="function")
def browser(request):
    browser = request.config.getoption("browser_name")
    if browser == "chrome":
        language = request.config.getoption("language")
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    elif browser == "firefox":
        language = request.config.getoption("language")
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
