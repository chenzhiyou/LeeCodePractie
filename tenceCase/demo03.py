from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com")
        self.driver.maximize_window()

    def test_prop(self):
        # 常用的属性
        print(self.driver.name)
        print(self.driver.current_url)
        print(self.driver.title)
        print(self.driver.window_handles)
        print(self.driver.page_source)
        self.driver.quit()

    def test_method(self):
        self.driver.find_element(By.ID, "kw").send_keys("selenium")
        self.driver.find_element(By.ID, "su").click()
        sleep(2)
        self.driver.back()
        sleep(2)
        self.driver.refresh()
        sleep(2)
        self.driver.forward()
        sleep(2)
        # 只关闭当前tab
        self.driver.close()
        # 关闭浏览器
        self.driver.quit()

    def test_window(self):
        self.driver.find_element(By.LINK_TEXT, "新闻").click()
        window = self.driver.window_handles
        print(window)
        for w in window:
            self.driver.switch_to.window(w)
            sleep(2)


if __name__ == "__main__":
    case = TestCase()
    # case.test_prop()
    # case.test_method()
    case.test_window()
