import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def test_e2e2(browserInstance):

    driver = browserInstance
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.find_element(By.LINK_TEXT, "Shop").click()
    products = driver.find_elements(By.XPATH, "//app-card-list[@class='row']/app-card")

    for product in products:
        product_name = product.find_element(By.XPATH, "div/div/h4/a").text
        if product_name == "Blackberry":
            product.find_element(By.XPATH, "div/div[2]/button").click()

    driver.find_element(By.CSS_SELECTOR, "a[class*=btn-primary]").click()
    driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
    driver.find_element(By.XPATH, "//input[@id='country']").send_keys("india")
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, 'India')))
    driver.find_element(By.LINK_TEXT, "India").click()
    driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    sucess_text = driver.find_element(By.CLASS_NAME, "alert").text
    print(sucess_text)

    assert "Success! Thank you!" in sucess_text
    #

    time.sleep(2)