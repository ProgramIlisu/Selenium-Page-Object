import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action="store",
        default="en",
        help="Choose language"
    )


@pytest.fixture(scope="function")
def browser(request):
    options = Options()
    options.add_argument("--lang=" + request.config.getoption("--language"))
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()

