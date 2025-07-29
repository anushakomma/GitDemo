import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/iframe")
driver.implicitly_wait(10)

driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID, "tinymce").clear()
time.sleep(5)
driver.find_element(By.ID, "tinymce").send_keys("anusha")
driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR,"h3").text)

