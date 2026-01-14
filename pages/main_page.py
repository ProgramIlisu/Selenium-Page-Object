from .base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import MainPageLocators

class MainPage(BasePage):

    def open_my_account_menu(self):
        my_account = self.browser.find_element(*MainPageLocators.MY_ACCOUNT)
        ActionChains(self.browser).move_to_element(my_account).perform()

    def should_be_login_link(self):
        self.open_my_account_menu()
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), \
            "Login link is not presented"




