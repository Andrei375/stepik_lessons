from selenium import webdriver
from sys import argv
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


script_name, link = argv

browser = webdriver.Chrome()
browser.get(link)

button1 = browser.find_element_by_id('book')
WebDriverWait(browser, 13).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
)
button1.click()

find_x = browser.find_element_by_id('input_value')
x_value = int(find_x.text)
y = calc(x_value)

input_answer = browser.find_element_by_id('answer')
input_answer.send_keys(y)

click_submit = browser.find_element_by_id('solve')
click_submit.click()

# python module_3/lesson6_step8.py http://suninjuly.github.io/explicit_wait2.html
