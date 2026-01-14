from selenium.webdriver.common.by import By
from pages.main_page import MainPage
from pages.login_page import LoginPage

def test_guest_can_go_to_login_page(browser): # Этот тест проверяет переход
    link = "https://ecommerce-playground.lambdatest.io/index.php?route=common/home"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу

    # ТОЛЬКО проверка наличия ссылки
    page.should_be_login_link()         # выполняем метод страницы — переходим на страницу логина

