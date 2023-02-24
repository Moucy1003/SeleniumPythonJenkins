from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
filePath = "C:\\Users\\MOUMMAND\\PycharmProjects\\SeleniumPythonProject\\driver\\chromedriver.exe"
driver = webdriver.Chrome(filePath)
time.sleep(1)
driver.get("https://www.google.com")
time.sleep(1)

# Search Option
search_box = driver.find_element_by_name("q")
search_box.send_keys("chocolate")
search_box.send_keys(Keys.RETURN)

driver.quit()