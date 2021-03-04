import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(5)

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("https://stepik.org/lesson/25969/step/12")
time.sleep(5)

# Метод find_element_by_css_selector позволяет найти нужный элемент на сайте, указав путь к нему.
# Способы поиска элементов мы обсудим позже
# Ищем поле для ввода текста
textarea = driver.find_element_by_css_selector(".textarea")

# Напишем текст ответа в найденное поле
textarea.send_keys("get()")
time.sleep(5)

# Найдем кнопку, которая отправляет введенное решение
submit_button = driver.find_element_by_css_selector(".submit-submission")

# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
submit_button.click()
time.sleep(5)

# После выполнения всех действий мы не должны забыть закрыть окно браузера
driver.quit()

# Создадим виртуальное окружение:
# python -m venv selenium_env
# Запустим созданный для нас приложением venv файл activate.bat, чтобы активировать окружение:
# selenium_env\Scripts\activate.bat
# Деактивация окружения
# selenium_env\Scripts\deactivate.bat
# Запускаем интерпретатор Python
# python
# выход из интерпретатора
# exit()
# Устанавливаем Selenium
# pip install selenium==3.14.0
# Устанавливаем PyTest
# pip install pytest==5.1.1
# Запуск тестов через PyTest
# pytest test_abs_project.py
# Сохраняем все версии пакетов в специальный файл requirements.txt.
# pip freeze > requirements.txt
# Устанавливаем все пакеты в новом окружении одной командой!
# pip install -r requirements.txt
