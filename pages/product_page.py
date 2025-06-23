from selenium.webdriver.common.by import By
from .base_page import BasePage

class ProductPage(BasePage):
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success .alertinner strong")
    BASKET_TOTAL = (By.CSS_SELECTOR, ".basket-mini")
    
    def add_product_to_basket(self):
        self.browser.find_element(*self.ADD_TO_BASKET_BUTTON).click()
    
    def get_product_name(self):
        return self.browser.find_element(*self.PRODUCT_NAME).text
    
    def get_success_message(self):
        return self.browser.find_element(*self.SUCCESS_MESSAGE).text
    
    def get_product_price(self):
        return self.browser.find_element(*self.PRODUCT_PRICE).text
    
    def get_basket_total(self):
        basket_text = self.browser.find_element(*self.BASKET_TOTAL).text
        # Например, текст: "Basket total: £9.99"
        # Нужно извлечь цену из текста:
        return basket_text.split("£")[-1].strip()
    
    def solve_quiz_and_get_code(self):
        import math
        from selenium.common.exceptions import NoAlertPresentException
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
