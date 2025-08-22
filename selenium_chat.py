from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time

# Настройка опций Firefox
firefox_options = FirefoxOptions()
firefox_options.add_argument("--proxy-server=socks5://151.242.117.99")  # Адрес твоего VPN
firefox_options.add_argument("-private")  # Запуск в приватном режиме

# Укажи путь к GeckoDriver
service = FirefoxService(executable_path='GeckoDriver/geckodriver')  # Путь к GeckoDriver

# Инициализация драйвера
driver = webdriver.Firefox(service=service, options=firefox_options)

# Открытие сайта с чатом
driver.get('https://chat-ai.one/#chat')

# Ждем загрузки страницы
time.sleep(5)

# Найди поле ввода чата по ID
input_field = driver.find_element(By.ID, 'user-input')  # ID поля ввода

# Введи текст
input_field.send_keys('привет негрик')

# Нажми Enter
input_field.send_keys(Keys.RETURN)

# Ждем ответа
time.sleep(5)

# Найди контейнер с сообщениями по ID
messages_container = driver.find_element(By.ID, 'chat-messages')  # ID контейнера с сообщениями

# Найди все сообщения в контейнере
messages = messages_container.find_elements(By.TAG_NAME, 'div')

# Предположим, что последнее сообщение — это ответ бота
last_message = messages[-1]

# Выведи ответ
print(last_message.text)

# Закрытие браузера
driver.quit()
