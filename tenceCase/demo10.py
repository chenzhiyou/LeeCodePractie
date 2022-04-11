from selenium import webdriver
from time import sleep
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = "file:///" + path + "/test_wait.html"
        self.driver.get(file_path)

    def test_wait(self):
        self.driver.find_element(By.NAME, "btn").click()

#         显示等待
        wait = WebDriverWait(self.driver, 3)
        # loc = self.driver.find_element(By.ID, "id2")
        wait.until(expected_conditions.text_to_be_present_in_element((By.ID, "id2"), 'id2'))
        print("ok")


if __name__ == "__main__":
    case = TestCase()
    case.test_wait()
    case.driver.quit()
