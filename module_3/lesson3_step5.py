from selenium import webdriver
from sys import argv
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


script_name, link = argv

browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_id('input_value')
x = x_element.text
y = calc(x)

input_answer = browser.find_element_by_id('answer')
input_answer.send_keys(y)

check_checkbox = browser.find_element_by_id('robotCheckbox')
check_checkbox.click()

click_rbutton = browser.find_element_by_id('robotsRule')
click_rbutton.click()

click_submit = browser.find_element_by_class_name('btn')
click_submit.click()

# python module_3/lesson3_step5.py http://suninjuly.github.io/math.html
