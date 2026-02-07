from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def should_not_have_products(self):
        assert not self.is_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket contains products, but should be empty"

    def should_have_empty_basket_text(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), "Empty basket message is not present"
