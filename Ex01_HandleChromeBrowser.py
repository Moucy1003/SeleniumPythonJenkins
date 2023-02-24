import unittest
from selenium import webdriver
import time
class MyTestCase(unittest.TestCase):
    def test_launch_browser(self):
        filePath = "C:\\Users\\MOUMMAND\\PycharmProjects\\SeleniumPythonProject\\driver\\chromedriver.exe"

        driver = webdriver.Chrome(filePath)
        time.sleep(1)
        driver.quit()
        if __name__ == '__main__':
            unittest.main()