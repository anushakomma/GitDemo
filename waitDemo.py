import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
List_1 =[]
list_2 = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.XPATH,"//input[@type='search']").send_keys("ber")
time.sleep(2)
products = driver.find_elements(By.XPATH,"//div[@class='products']/div")
print(len(products))

vegs = driver.find_elements(By.XPATH,"//div[@class='product']/h4")

for veg in vegs:
    nameveg =veg.text
    List_1.append(nameveg)

print(List_1)
buttons = driver.find_elements(By.CSS_SELECTOR,"div[class='product-action'] button")
for button in buttons:
    button.click()

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR,"input[class='promoCode']").send_keys("rahulshettyacademy")

driver.find_element(By.CLASS_NAME,"promoBtn").click()

wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"promoInfo")))

text = driver.find_element(By.CSS_SELECTOR,".promoInfo").text
print(text)
prices =driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")
sum =0
for price in prices:
    sum = sum + int(price.text)
print(sum)
totalAmt = driver.find_element(By.CLASS_NAME,"totAmt").text
assert sum == int(totalAmt)
Disscountper = driver.find_element(By.CSS_SELECTOR,".discountPerc").text
DisscountAmt = driver.find_element(By.CSS_SELECTOR,".discountAmt").text
print(Disscountper)

assert sum > float(DisscountAmt)

assert list_2 == List_1


