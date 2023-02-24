import unittest
from selenium import webdriver
import time
class MyTestCase(unittest.TestCase):
    def test01(self):
        filePath = "C:\\Users\\MOUMMAND\\PycharmProjects\\SeleniumPythonProject\\driver\\chromedriver.exe"
        driver = webdriver.Chrome(filePath)
        time.sleep(1)
        driver.maximize_window()
        time.sleep(1)
        driver.fullscreen_window()
        time.sleep(1)
        driver.quit()
        if __name__ == '__main__':
            unittest.main()
