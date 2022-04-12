from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.baidu.com")

    def test_script(self):
        self.driver.execute_script("alert('test')")
        sleep(2)
        self.driver.switch_to.alert.accept()

    def test_script2(self):
        js = 'return document.title'
        title = self.driver.execute_script(js)
        print(title)

    def test_script3(self):
        js = 'var q = document.getElementById("kw"); q.style.border="2px solid red"'
        self.driver.execute_script(js)
        sleep(2)

    def test_script4(self):
        self.driver.find_element(By.ID, "kw").send_keys("selenium")
        self.driver.find_element(By.ID, "su").click()
        js = "window.scrollTo(0, document.body.scrollHeight)"
        self.driver.execute_script(js)
        sleep(2)


if __name__ == "__main__":
    case = TestCase()
    case.test_script4()
    # case.driver.quit()
