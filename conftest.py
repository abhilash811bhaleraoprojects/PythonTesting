import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )


@pytest.fixture(scope="function")
def browserInstance(request):
    browser_name = request.config_options("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
        driver.implicitly_wait(4)
        driver.get("https://rahulshettyacademy.com/angularpractice/")
        driver.maximize_window()
    yield driver