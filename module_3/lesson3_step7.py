from selenium import webdriver
from sys import argv
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))  # ln(abs(12*sin(x)))


script_name, link = argv

browser = webdriver.Chrome()
browser.get(link)

picture = browser.find_element_by_id('treasure')
x_value = picture.get_attribute('valuex')
y = calc(x_value)

input_answer2 = browser.find_element_by_id('answer')
input_answer2.send_keys(y)

check_checkbox2 = browser.find_element_by_id('robotCheckbox')
check_checkbox2.click()

click_rbutton2 = browser.find_element_by_id('robotsRule')
click_rbutton2.click()

click_submit2 = browser.find_element_by_class_name('btn')
click_submit2.click()

# python module_3/lesson3_step7.py http://suninjuly.github.io/get_attribute.html
