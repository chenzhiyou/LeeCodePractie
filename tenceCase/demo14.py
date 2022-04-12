from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://sahitest.com/demo/framesTest.htm")

    def test_frame(self):
        top = self.driver.find_element(By.NAME, 'top')
        self.driver.switch_to.frame(top)
        self.driver.find_element(By.XPATH, "").click()
        self.driver.switch_to.default_content()
        second = self.driver.find_element(By.XPATH, "")
        self.driver.switch_to.frame(second)


if __name__ == "__main__":
    case = TestCase()
    case.driver.quit()
