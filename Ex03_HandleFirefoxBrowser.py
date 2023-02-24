import unittest
from selenium import webdriver
import time
class MyTestCase(unittest.TestCase):
    def test_launch_browser(self):
        filePath = "C:\\Users\\MOUMMAND\\PycharmProjects\\SeleniumPythonProject\\driver\\geckodriver.exe"
        driver = webdriver.Firefox(filePath)
        time.sleep(1)
        driver.quit()
        if __name__ == '__main__':
            unittest.main()