from selenium import webdriver
driver= webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

Chrome_Options= webdriver.ChromeOptions()
Chrome_Options.add_argument("headless")
Chrome_Options.add_argument("--ignore-certificate-errors")

driver= webdriver.Chrome(options=Chrome_Options)
#driver= webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.implicitly_wait(5)
driver.execute_script("window.scrollBy(0,700);")
driver.get_screenshot_as_file("image1.png")
