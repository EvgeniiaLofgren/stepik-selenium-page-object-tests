from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        btn.click()

    def should_be_correct_product_added(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        added_product_name = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_ADDED).text
        assert product_name == added_product_name, \
            f"Expected '{product_name}', but got '{added_product_name}'"

    def should_be_correct_basket_total(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_total = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_TOTAL).text
        assert product_price == basket_total, \
            f"Expected basket total '{product_price}', but got '{basket_total}'"
