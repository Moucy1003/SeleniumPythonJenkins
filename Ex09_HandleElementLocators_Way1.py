import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
class MyTestCase(unittest.TestCase):
    def test01(self):
        filePath = "C:\\Users\\MOUMMAND\\PycharmProjects\\SeleniumPythonProject\\driver\\chromedriver.exe"
        url = "https://parabank.parasoft.com/parabank/index.htm"
        driver = webdriver.Chrome(filePath)
        time.sleep(1)
        driver.get(url)
        time.sleep(1)

        # driver.find_element(By.LINK_TEXT, "About Us") - It will identify the About Us link element on web page
        # click() - It will perform click operation on About Us link element

        # Linktext
        driver.find_element(By.LINK_TEXT, "About Us").click()

        time.sleep(2)

        # PartialLinkText
        driver.find_element(By.PARTIAL_LINK_TEXT, "Ser").click()

        time.sleep(2)

        # LinkText
        driver.find_element(By.LINK_TEXT, "Register").click()

        time.sleep(2)
        # Name
        driver.find_element(By.NAME, "customer.firstName").send_keys("John")
        time.sleep(2)

        # Id
        driver.find_element(By.ID, "customer.lastName").send_keys("Adam")
        time.sleep(1)

        driver.quit()
        if __name__ == '__main__':
            unittest.main()