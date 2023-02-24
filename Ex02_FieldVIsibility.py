from selenium import webdriver
import time
filePath = "C:\\Users\\MOUMMAND\\PycharmProjects\\SeleniumPythonProject\\driver\\chromedriver.exe"
driver = webdriver.Chrome(filePath)
time.sleep(1)
driver.get("https://www.google.com/")
time.sleep(1)
search_box = driver.find_element_by_class_name("gLFyf")
search_button = driver.find_element_by_class_name("gNO89b")
lucky_button = driver.find_element_by_class_name("RNmpXc")
if search_box.is_displayed() and search_button.is_displayed() and lucky_button.is_displayed():
    print("All fields on the Google landing page are visible")
else:
    print("Some fields on the Google landing page are not visible")
driver.quit()
