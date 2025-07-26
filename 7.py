from selenium import webdriver
from selenium.webdriver.common.by import By
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# функция для вычисления результата
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

# инициализация драйвера
browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)

try:
    # ждем, пока цена не станет $100 (не менее 12 секунд)
    wait = WebDriverWait(browser, 20)
    price_element = wait.until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # нажимаем кнопку "Book"
    book_button = browser.find_element(By.ID, "book")
    book_button.click()

    # решаем математическую задачу
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    result = calc(x)

    # вводим ответ в поле
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(result)

    # отправляем решение
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

    time.sleep(3)

finally:
    # закрываем браузер
    browser.quit()
