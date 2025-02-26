from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from test_data.login_data import login_email, password_mail, password_phone, login_phone
from utils.BaseClass import BaseClass


class AuthorizationForm(BaseClass):
    open_login = (By.XPATH, "//a[contains(@href, 'auth-step=login')][3]")
    email_form = (By.NAME, "email")
    phone_form = (By.CLASS_NAME, "PhoneInputInput")
    password_form = (By.NAME, "password")
    sign_in = (By.CSS_SELECTOR, "button[type='submit']")
    phone_tab = (By.XPATH, "//button[contains(text(), 'Телефон') or contains(text(), 'Phone')]")

    def __init__(self, driver):
        self.driver = driver

    def login_popup(self):
        return self.wait_for_element(self.open_login, condition="clickable").click()

    def input_email(self):
        return self.wait_for_element(self.email_form, condition="clickable").send_keys(login_email)

    def input_password_mail(self):
        return self.wait_for_element(self.password_form, condition="clickable").send_keys(password_mail)

    def select_phone_tab(self):
        return self.wait_for_element(self.phone_tab, condition="clickable").click()

    def phone_input_clean(self):
        return self.wait_for_element(self.phone_form, condition="clickable").send_keys(Keys.BACKSPACE)

    def login_phone(self):
        return self.wait_for_element(self.phone_form, condition="clickable").send_keys(login_phone)

    def input_password_phone(self):
        return self.wait_for_element(self.password_form, condition="clickable").send_keys(password_phone)

    def sing_in(self):
        return self.wait_for_element(self.sign_in, condition="clickable").click()
