from selenium import webdriver
from sys import argv
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

script_name, link = argv

browser = webdriver.Chrome()
browser.get(link)

find_x = browser.find_element_by_id('input_value')
x_value = int(find_x.text)
y = calc(x_value)

input_answer = browser.find_element_by_id('answer')
input_answer.send_keys(y)

check_checkbox = browser.find_element_by_id('robotCheckbox')
check_checkbox.click()

click_submit = browser.find_element_by_class_name('btn')
browser.execute_script("return arguments[0].scrollIntoView(true);", click_submit)

click_rbutton = browser.find_element_by_id('robotsRule')
click_rbutton.click()

click_submit.click()


# python module_3/lesson4_step6.py http://SunInJuly.github.io/execute_script.html
