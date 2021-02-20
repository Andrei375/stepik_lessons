from selenium import webdriver

login_page_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
main_page_link = "http://selenium1py.pythonanywhere.com/en-gb/"
input_login_locator = "#id_login-username"
input_password_locator = "#id_login-password"
welcom_icon_locator = ".alertinner"
submit_login_and_password_button_locator = "[name='login_submit']"


def test_login():
    # Data
    login = 'kosmos09@tut.by'
    password = 'iXXeu22DPA4jv9Z'
    search_text = 'Рады видеть вас снова'

    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(login_page_link)

        # Act
        input_login = browser.find_element_by_css_selector(input_login_locator)
        input_login.send_keys(login)

        input_password = browser.find_element_by_css_selector(input_password_locator)
        input_password.send_keys(password)

        browser.find_element_by_css_selector(submit_login_and_password_button_locator).click()

        # Assert
        welcom_icon = browser.find_element_by_css_selector(welcom_icon_locator)
        assert main_page_link == browser.current_url, \
            "there is no transition to the main page after login"
        assert search_text in welcom_icon.text, "failed welcom alert icon on the main page"

    finally:
        browser.quit()


test_login()
# python module_3\test_sample.py
