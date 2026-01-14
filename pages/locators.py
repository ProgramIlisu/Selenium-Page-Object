from selenium.webdriver.common.by import By

class MainPageLocators:
    MY_ACCOUNT = (By.CSS_SELECTOR, "a.nav-link.dropdown-toggle[href*='route=account/account']")
    LOGIN_LINK = (By.XPATH, "//a[contains(@href, 'route=account/login')]")
    REGISTER_LINK = (By.XPATH, ".//a[contains(@href, 'route=account/register')]")
    LOGIN_LINK = (By.XPATH, ".//a[contains(@href, 'route=account/login')]")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "input-email")
    REGISTER_LINK = (By.LINK_TEXT, "Register")

