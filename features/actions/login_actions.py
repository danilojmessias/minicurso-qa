import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from features.pages.login_page import LoginPage

class LoginActions:
    def __init__(self, driver):
        self.driver = driver

    def fill_all_fields(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LoginPage.name_input)).send_keys("nome caraii")

    def click_on_submit(self):
        self.submit_button.click()
        time.sleep(10)