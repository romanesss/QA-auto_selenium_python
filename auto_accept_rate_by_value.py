from selenium import webdriver
import time , math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calcilart (x) :
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    cost = WebDriverWait(browser,12).until(
        EC.text_to_be_present_in_element((By.ID,"price"),"$100"))
    button = browser.find_element_by_id("book").click()

    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    value = browser.find_element_by_id("input_value")
    x = value.text
    summa = calcilart(x)

    answer_box = browser.find_element_by_id('answer').send_keys(summa)

    submit_click = browser.find_element_by_css_selector("[type='submit']").click()




    ##successful test
    #message = browser.find_element_by_id("verify_message")
    #assert "successful" in message.text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()