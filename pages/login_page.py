from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    REGISTER_EMAIL = (By.ID, "id_registration-email")
    REGISTER_PASSWORD1 = (By.ID, "id_registration-password1")
    REGISTER_PASSWORD2 = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*self.REGISTER_EMAIL)
        password1_input = self.browser.find_element(*self.REGISTER_PASSWORD1)
        password2_input = self.browser.find_element(*self.REGISTER_PASSWORD2)
        register_btn = self.browser.find_element(*self.REGISTER_BUTTON)

        email_input.send_keys(email)
        password1_input.send_keys(password)
        password2_input.send_keys(password)
        register_btn.click()
