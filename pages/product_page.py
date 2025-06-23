from selenium.webdriver.common.by import By
from .base_page import BasePage

class ProductPage(BasePage):
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(1) .alertinner strong")
    MESSAGE_PRICE = (By.CSS_SELECTOR, "#messages .alert-info .alertinner strong")

    def add_product_to_basket(self):
        self.browser.find_element(*self.ADD_TO_BASKET_BUTTON).click()

    def get_product_name(self):
        return self.browser.find_element(*self.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*self.PRODUCT_PRICE).text

    def is_message_about_adding_present(self):
        return self.is_element_present(*self.MESSAGE_ABOUT_ADDING)

    def get_name_in_message(self):
        return self.browser.find_element(*self.MESSAGE_ABOUT_ADDING).text

    def get_price_in_message(self):
        return self.browser.find_element(*self.MESSAGE_PRICE).text
