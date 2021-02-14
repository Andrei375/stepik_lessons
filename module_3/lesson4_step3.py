from selenium import webdriver
from sys import argv
from selenium.webdriver.support.ui import Select


def calc(a, b):
    return str(a + b)


script_name, link = argv

browser = webdriver.Chrome()
browser.get(link)

find_a = browser.find_element_by_id('num1')
a_value = int(find_a.text)

find_b = browser.find_element_by_id('num2')
b_value = int(find_b.text)
y = calc(a_value, b_value)

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(str(y))

click_submit = browser.find_element_by_class_name('btn')
click_submit.click()

# python module_3/lesson4_step3.py http://suninjuly.github.io/selects1.html
