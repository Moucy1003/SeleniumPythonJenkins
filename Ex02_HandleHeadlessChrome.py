import unittest
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
class MyTestCase(unittest.TestCase):
    def test_launch_browser(self):
        filePath = "C:\\Users\\MOUMMAND\\PycharmProjects\\SeleniumPythonProject\\driver\\chromedriver.exe"
        chromeOptions = Options()
        chromeOptions.add_argument("--headless")
        driver = webdriver.Chrome(filePath, chrome_options=chromeOptions)
        time.sleep(1)
        driver.quit()
        if __name__ == '__main__':
            unittest.main()
