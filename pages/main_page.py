from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    def should_be_login_link(self):
        try:
            self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        except NoSuchElementException:
            assert False, "Login link is not present on the page"
