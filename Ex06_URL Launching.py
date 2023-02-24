import unittest
from selenium import webdriver
import time
class MyTestCase(unittest.TestCase):
    def test01(self):
        filePath = "C:\\Users\\MOUMMAND\\PycharmProjects\\SeleniumPythonProject\\driver\\chromedriver.exe"
        url = "https://parabank.parasoft.com/parabank/index.htm"
        driver = webdriver.Chrome(filePath)
        time.sleep(1)
        driver.get(url)
        time.sleep(1)
        driver.quit()
        if __name__ == '__main__':
            unittest.main()