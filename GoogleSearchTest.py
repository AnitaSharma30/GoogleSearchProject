from selenium import webdriver
import unittest
import HtmlTestRunner

class GoogleSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\\browser\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_automationstepbystep(self):
        self.driver.get("https://www.google.com/")
        self.driver.find_element_by_name("q").send_keys("Automation step by step")
        self.driver.find_element_by_name("btnK").click()

# To show the error we passed the wrong button id(btnK1). Correct Button id is btnK.
    def test_seleniumtutorials(self):
        self.driver.get("https://www.google.com/")
        self.driver.find_element_by_name("q").send_keys("Selenium tutorial")
        self.driver.find_element_by_name("btnK1").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Anita/PycharmProjects/PythonTest/Reports'))

