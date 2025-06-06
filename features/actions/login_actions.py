import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from features.pages.login_page import LoginPage

class LoginActions:
    def __init__(self, driver):
        self.driver = driver

    def fill_all_fields(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LoginPage.name_input)).send_keys("Danilo Messias")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LoginPage.email_input)).send_keys("danilo@email.com")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LoginPage.birth_data_input)).send_keys("16/08/2000")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LoginPage.password_input)).send_keys("12345678")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LoginPage.password_confirm_input)).send_keys("12345678")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LoginPage.terms_checkbox)).click()

    def fill_all_fields_without_name(self): #função para preencher com o nome vázio
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LoginPage.email_input)).send_keys("danilo@email.com")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LoginPage.birth_data_input)).send_keys("16/08/2000")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LoginPage.password_input)).send_keys("12345678")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LoginPage.password_confirm_input)).send_keys("12345678")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LoginPage.terms_checkbox)).click()          

    def click_on_submit(self):
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LoginPage.submit_button)).click()
    
    def validate_success_message(self):
        time.sleep(2)
        text = WebDriverWait(self.driver, 4).until(EC.visibility_of_element_located(LoginPage.success_message)).text
        assert text == "Cadastro realizado com sucesso!"
    
    def validate_success_message_not_present(self): #validando que não exista mensagem de sucesso
        try:
            WebDriverWait(self.driver, 4).until(
                EC.invisibility_of_element_located(LoginPage.success_message)
            )
        except TimeoutException:
            raise AssertionError("A mensagem de sucesso foi exibida, mas não deveria.")
