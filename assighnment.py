
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.implicitly_wait(5)

driver.find_element(By.CLASS_NAME,"blinkingText").click()
windowsOpened = driver.window_handles

driver.switch_to.window(windowsOpened[1])
message = driver.find_element(By.CLASS_NAME,"red").text
email = [word for word in message.split() if '@' in word][0]

driver.switch_to.window(windowsOpened[0])
driver.find_element(By.ID,"username").send_keys(email)
driver.find_element(By.ID,"password").send_keys("12345")
dropdown = Select(driver.find_element(By.XPATH,"//select[@class='form-control']"))
dropdown.select_by_visible_text("Teacher")
driver.find_element(By.ID,"terms").click()
driver.find_element(By.ID,"signInBtn").click()

wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,".alert")))
print(driver.find_element(By.CLASS_NAME,"alert").text)