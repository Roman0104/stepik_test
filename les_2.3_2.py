from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    new_window = browser.window_handles[1]  # берем имя второй вкладки
    browser.switch_to.window(new_window)  # переключаемся на вторую вкладку
    # решить капчу для роботов, чтобы получить число с ответом
    x_element = browser.find_element_by_css_selector(".nowrap#input_value") # Считаем строку с 'Х'
    x = x_element.text  # выдерним заначение 'X'
    y = calc(x)
    # Найдем куда и вставим значение 'y'
    input1 = browser.find_element_by_css_selector(".form-control#answer")
    input1.send_keys(y)
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()