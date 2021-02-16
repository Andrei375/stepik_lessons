# 1. Предусловия и настройка окружения (открытие браузера, установка дополнительных параметров);
# 2. Сами шаги теста;
# 3. Проверка на ожидаемый результат: например, на странице находится нужный текст или отображается соответствующий элемент
# (а может, мы просто убеждаемся, что перешли на корректный URL, - все зависит от того, как вы описывали свои тесты);
# 4. Пост-условия: например, закрытие браузера.
# Скрипт описан в виде функции; название тестовой функции соответствует шагам и проверкам в ее теле
# Скрипт использует концепцию ААА: блоки Arrange, Act, Assert визуально отделены друг от друга, содержимое блоков соответствует их названиям
# Названия используемых переменных соответствуют их содержимому
# Скрипт не содержит неиспользуемых переменных
# Скрипт не содержит захардкоженных значений (либо должно быть пояснение, почему хардкод уместен в данном случае)
# assert'ы содержат понятные и подробные сообщения о совершаемой проверке и ожидаемом результате

from selenium import webdriver

link1 = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
link2 = "http://selenium1py.pythonanywhere.com/en-gb/accounts/logout/"

browser = webdriver.Chrome()
browser.get(link1)

input_name = browser.find_element_by_id('id_login-username')
input_name.send_keys('kosmos09@tut.by')

input_password = browser.find_element_by_id('id_login-password')
input_password.send_keys('iXXeu22DPA4jv9Z')

click_submit = browser.find_element_by_name('login_submit')
click_submit.click()
# таким способом не получается сравнить страницу
assert link2 == browser.window_handles[1]

#browser.quit()

# python module_3\test_sample.py
