from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/ru/"
registration_email = "kosmos13@tut.by"
registration_password = "{j[jne[t7Ktn"
btn_login_selector = "#login_link"
btn_registration_selector = "[name='registration_submit']"
input_registration_email_selector = "#id_registration-email"
input_registration_password_selector = "#id_registration-password1"
input_repeat_registration_password_selector = "#id_registration-password2"
alert_icon_successful_registration_selector = ".alertinner"
search_text_when_registration_successful = "Спасибо за регистрацию"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_css_selector(btn_login_selector).click()

    browser.find_element_by_css_selector(input_registration_email_selector).send_keys(registration_email)
    browser.find_element_by_css_selector(input_registration_password_selector).send_keys(registration_password)
    browser.find_element_by_css_selector(input_repeat_registration_password_selector).send_keys(registration_password)
    browser.find_element_by_css_selector(btn_registration_selector).click()

    assert search_text_when_registration_successful in browser.find_element_by_css_selector(alert_icon_successful_registration_selector).text, "no alert icon with congratulation for successful registration"

finally:
    browser.quit()

# python module_4\part_2\code_sample.py
