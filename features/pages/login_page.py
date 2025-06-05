from selenium.webdriver.common.by import By

class LoginPage:
    name_input = (By.ID,"name")
    submit_button = (By.CSS_SELECTOR, "button.btn.btn-primary")