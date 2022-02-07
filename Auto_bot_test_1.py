from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time , math , os

def calcilart (x) :
    return str(math.log(abs(12*math.sin(int(x)))))

try:

    from selenium import webdriver

    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    click1 = browser.find_element_by_css_selector("[type='submit']").click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    #time.sleep(500)

    value = browser.find_element_by_id("input_value")
    x = value.text
    summa = calcilart(x)

    answer_box = browser.find_element_by_id('answer').send_keys(summa)

    submit_click = browser.find_element_by_css_selector("[type='submit']").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

