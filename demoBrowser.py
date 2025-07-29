import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from FindElementsTest import countries

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)


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

for country in countries:
    if country.text == "India":
        country.click()
        break
print(driver.find_element(By.ID,"autosuggest").get_attribute('value'))
#assert driver.find_element(By.ID,"autosuggest").get_attribute('value')== "India"


time.sleep(3)