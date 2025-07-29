import pytest
from pygments.lexer import default
from selenium.webdriver.chrome import webdriver
from selenium import webdriver



def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome",help= "run slow test"
    )

@pytest.fixture(scope="function")
def browserInstance(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name =="firefox":
        driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    yield driver