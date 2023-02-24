from selenium import webdriver
import time
filePath = "C:\\Users\\MOUMMAND\\PycharmProjects\\SeleniumPythonProject\\driver\\chromedriver.exe"
driver = webdriver.Chrome(filePath)
time.sleep(1)
driver.get("https://www.google.com")
time.sleep(1)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.refresh()
time.sleep(1)
driver.close()
driver.quit()
