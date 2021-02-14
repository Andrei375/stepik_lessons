import os
from selenium import webdriver
from sys import argv

script_name, link = argv

browser = webdriver.Chrome()
browser.get(link)

input_firstname = browser.find_element_by_name('firstname')
input_firstname.send_keys('Николай')

input_lastname = browser.find_element_by_name('lastname')
input_lastname.send_keys('Штирлиц')

input_email = browser.find_element_by_name('email')
input_email.send_keys('kosmos09@tut.by')

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
input_file = browser.find_element_by_id('file')
input_file.send_keys(file_path)

click_submit = browser.find_element_by_class_name('btn')
click_submit.click()

# python module_3/lesson4_step8.py http://suninjuly.github.io/file_input.html
