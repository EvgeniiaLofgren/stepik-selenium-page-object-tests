from selenium.webdriver.common.by import By
from .base_page import BasePage

class ProductPage(BasePage):
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main .price_color")
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    SUCCESS_MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages div.alertinner strong")
    BASKET_TOTAL_PRICE = (By.CSS_SELECTOR, ".basket-mini")

    def get_product_name(self):
        return self.browser.find_element(*self.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*self.PRODUCT_PRICE).text

    def add_product_to_basket(self):
        self.browser.find_element(*self.ADD_TO_BASKET_BUTTON).click()

    def should_be_correct_product_name_in_message(self, product_name):
        message_name = self.browser.find_element(*self.SUCCESS_MESSAGE_PRODUCT_NAME).text
        assert message_name == product_name, (
            f"Expected product name '{product_name}' but got '{message_name}'"
        )

    def should_be_correct_basket_price(self, product_price):
        basket_text = self.browser.find_element(*self.BASKET_TOTAL_PRICE).text
        assert product_price in basket_text, (
            f"Expected basket price to include '{product_price}', but got '{basket_text}'"
        )
