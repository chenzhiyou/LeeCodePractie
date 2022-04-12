from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # self.driver.get("http://sahitest.com/demo/clicks.htm")
        self.driver.get("https://www.baidu.com")

    def test_action_chains(self):
        action = ActionChains(self.driver)
        btn = self.driver.find_element(By.XPATH, "/html/body/form/input[2]")
        # 双击
        action.double_click(btn).perform()
        # 单击
        click_elm = self.driver.find_element(By.XPATH, "/html/body/form/input[3]")
        action.click(click_elm).perform()
        # 右击
        right_elm = self.driver.find_element(By.XPATH, "/html/body/form/input[4]")
        action.context_click(right_elm).perform()
        sleep(5)

    def test_key(self):
        kw = self.driver.find_element(By.ID, "kw")
        kw.send_keys("selenium")
        kw.send_keys(Keys.CONTROL, 'a')
        sleep(2)
        kw.send_keys(Keys.CONTROL, "v")
        sleep(2)


if __name__ == "__main__":
    case = TestCase()
    case.test_key()
    case.driver.quit()
