from selenium import webdriver
from sys import argv
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


script_name, link = argv

browser = webdriver.Chrome()
browser.get(link)

button1 = browser.find_element_by_css_selector('.btn.btn-primary')
button1.click()

confirm = browser.switch_to.alert
confirm.accept()

find_x = browser.find_element_by_id('input_value')
x_value = int(find_x.text)
y = calc(x_value)

input_answer = browser.find_element_by_id('answer')
input_answer.send_keys(y)

click_submit = browser.find_element_by_class_name('btn')
click_submit.click()

# python module_3/lesson5_step4.py http://suninjuly.github.io/alert_accept.html
