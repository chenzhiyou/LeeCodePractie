from selenium import webdriver
from time import sleep, strftime, localtime, time

from selenium.webdriver.common.by import By
import os


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com")

    def test_screenshot(self):
        self.driver.find_element(By.ID, "kw").send_keys("selenium")
        sleep(2)
        st = strftime("%Y-%m-%d-%H-%M-%S", localtime(time()))
        file_name = st + ".png"
        path = os.path.abspath("screenshot")
        file_path = path + '/' + file_name
        self.driver.save_screenshot(file_path)


if __name__ == "__main__":
    case = TestCase()
    case.test_screenshot()
    case.driver.quit()
