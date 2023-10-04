
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Site:
    def __init__(self, address):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get(address)
        time.sleep(5)

    def wait(self, seconds):
        return self.driver.implicitly_wait(seconds)

    def select_window(self):
        return self.driver.switch_to.active_element

    def find_element(self, mode, path):
        if mode == 'css':
            element = self.driver.find_element(By.CSS_SELECTOR, path)
        elif mode == 'xpath':
            element = self.driver.find_element(By.XPATH, path)
        else:
            element = None
        return element

    def get_element_property(self, mode, path, property):
        element = self.find_element(mode, path)
        return element.value_of_css_property(property)

    def close(self):
        self.driver.close()
