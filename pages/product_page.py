from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON
        ).click()

    def should_not_be_success_message(self):
        assert not self.is_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), "Success message is presented, but should not be"

