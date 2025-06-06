from selenium.webdriver.common.by import By

class LoginPage:
    name_input = (By.ID,"name")
    email_input = (By.ID,"email")
    birth_data_input = (By.ID,"birthDate")
    password_input = (By.ID,"password")
    password_confirm_input = (By.ID,"passwordConfirm")
    terms_checkbox = (By.ID,"terms")
    terms_href = (By.XPATH,'//*[@id="cadastroForm"]/div[6]/label/a')
    submit_button = (By.XPATH, '//*[@id="cadastroForm"]/button')
    success_message = (By.ID, "mensagem")