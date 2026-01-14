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

    def go_to_login_page(self):
        # 1. Ждём My Account
        my_account = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(MainPageLocators.MY_ACCOUNT)
        )

        # 2. Наводим курсор (раскрываем меню)
        ActionChains(self.browser).move_to_element(my_account).perform()

        # 3. Ждём, пока Login станет кликабельным
        login_link = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(MainPageLocators.LOGIN_LINK)
        )

        # 4. Кликаем Login
        login_link.click()





