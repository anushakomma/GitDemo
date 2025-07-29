import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
name = "Anusha"
driver.find_element(By.ID, "name").send_keys(name)
driver.find_element(By.CSS_SELECTOR, "#confirmbtn").click()
alert = driver.switch_to.alert
alerttext = alert.text
time.sleep(2)
print(alerttext)
alert.accept()
time.sleep(2)
#alert.dismiss()
assert name in alerttext
