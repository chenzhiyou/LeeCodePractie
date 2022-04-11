import os

from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
# 掌握CheckBox和radiobutton的定位技巧


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))
        print(path)
        file_path = 'file:///' + path + '/forms2.html'
        print(file_path)
        self.driver.get(file_path)

    def test_checkbox(self):
        swimming = self.driver.find_element(By.NAME, "swimming")
        if not swimming.is_selected():
            swimming.click()
        self.driver.find_element(By.NAME, "reading").click()
        sleep(3)
        swimming.click()
        sleep(3)
        self.driver.quit()

    def test_radio(self):
        radio_list = self.driver.find_elements(By.NAME, "gender")
        radio_list[0].click()
        sleep(3)
        radio_list[1].click()
        sleep(3)
        self.driver.quit()


if __name__ == "__main__":
    case = TestCase()
    # case.test_checkbox()
    case.test_radio()
