import pytest ,math , time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import warnings

@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print('\nquit browser..')
    if words != '' :
        print("\nThe part of text : "+words)
    browser.quit()

def answer():
    answer = str(math.log(int(time.time())))
    return answer

class TestMainPage():
    first_link   = "https://stepik.org/lesson/236895/step/1"
    second_link  = "https://stepik.org/lesson/236896/step/1"
    third_link   = "https://stepik.org/lesson/236897/step/1"
    fourth_link  = "https://stepik.org/lesson/236898/step/1"
    fifth_link   = "https://stepik.org/lesson/236899/step/1"
    sixt_link    = "https://stepik.org/lesson/236903/step/1"
    seventh_link = "https://stepik.org/lesson/236904/step/1"
    eight_link   = "https://stepik.org/lesson/236905/step/1"

    @pytest.mark.parametrize('link',[first_link,sixt_link,third_link,fourth_link,fifth_link,sixt_link,seventh_link,eight_link])
    def test_input(self,browser,link):
        browser.get(link)
        browser.implicitly_wait(10)

        input_area = browser.find_element_by_css_selector("[class='ember-text-area ember-view textarea string-quiz__textarea']")
        input_area.send_keys(answer())


        submit_button = browser.find_element_by_css_selector('[class="submit-submission"]').click()


        correct_button = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'[class="smart-hints__hint"]')))

        global words
        words = ''
        if correct_button.text != 'Correct!' :
            words += correct_button.text
        assert correct_button.text == 'Correct!'

