from selenium import webdriver
import time
filePath = "C:\\Users\\MOUMMAND\\PycharmProjects\\SeleniumPythonProject\\driver\\chromedriver.exe"
driver = webdriver.Chrome(filePath)
time.sleep(1)
driver.get("https://www.google.com")
time.sleep(1)


# Check that the page title is "Google"
if driver.title == "Google":
    print("User successfully navigated to the Google landing page")
else:
    print("User did not navigate to the Google landing page")
driver.quit()
