# Page Object Project (Selenium + PyTest)

Учебный проект по автоматизации UI-тестирования веб-приложения с использованием **Selenium WebDriver**, **PyTest** и паттерна **Page Object Model**.

Проект реализован в рамках обучения и демонстрирует:
- корректную структуру Page Object
- группировку тестов
- использование фикстур
- работу с негативными проверками
- маркировку тестов для ревью

---

## 📁 Структура проекта

---
Page_Object_Project/
│
├── pages/
│ ├── init.py
│ ├── base_page.py
│ ├── main_page.py
│ ├── product_page.py
│ ├── basket_page.py
│ ├── login_page.py
│ └── locators.py
│
├── test_main_page.py
├── test_product_page.py
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
---

---

## 🧩 Используемые технологии

- Python 3.x  
- Selenium WebDriver  
- PyTest  
- Page Object Model  

---

## ⚙️ Установка и подготовка окружения

1. Клонировать репозиторий:
```bash
git clone <repo_url>
cd Page_Object_Project

    Установить зависимости:

pip install -r requirements.txt

Содержимое requirements.txt:

pytest==5.1.1
selenium==3.14.0

▶️ Запуск тестов
Запуск всех тестов:

pytest -v

Запуск тестов для ревью:

pytest -v --tb=line --language=en -m need_review

🏷 Используемые метки PyTest

Метки зарегистрированы в pytest.ini.

    need_review — тесты, обязательные для проверки

    login_guest — тесты перехода на страницу логина

    login — тесты авторизованных пользователей

🧪 Покрываемые сценарии
Гость:

    добавление товара в корзину

    переход на страницу логина

    пустая корзина при переходе без товаров

Авторизованный пользователь:

    регистрация нового пользователя

    добавление товара в корзину

    проверка успешной авторизации

🧱 Архитектура Page Object

    ❌ В тестах нет assert

    ✅ Все проверки и действия вынесены в Page Object

    ✅ Все селекторы находятся в locators.py

    ✅ Используется наследование от BasePage

⚠️ Примечание

Проект использует учебный сайт
http://selenium1py.pythonanywhere.com

В некоторых регионах сайт может быть недоступен без VPN.
✅ Статус проекта

✔ Все обязательные тесты реализованы
✔ Структура соответствует Page Object
✔ Код подготовлен для peer-review


Учебный проект
Автоматизация тестирования (Selenium + PyTest)
