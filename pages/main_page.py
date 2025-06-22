from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .login_page import LoginPage

class MainPage(BasePage):

    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        try:
            alert = self.browser.switch_to.alert
            alert.accept()
        except Exception:
            # if alert did not appear, continue
            pass
        # return LoginPage(browser=self.browser, url=self.browser.current_url)
