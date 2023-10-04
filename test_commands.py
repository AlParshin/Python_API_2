
from module import Site
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest


def test_find():

    site = Site('https://test-stand.gb.ru/login')
    login = '/html/body/div/main/div/div/div/form/div[1]/label/input'
    password = '/html/body/div/main/div/div/div/form/div[2]/label/input'
    title_input = '/html/body/div/main/div/div/form/div/div/div[1]/div/label/input'
    description = '/html/body/div/main/div/div/form/div/div/div[2]/div/label/span/textarea'
    content = '/html/body/div/main/div/div/form/div/div/div[3]/div/label/span/textarea'
    login = site.find_element('xpath', login)
    login.send_keys("CatKate11111")
    password = site.find_element('xpath', password)
    password.send_keys("cdeca16eb7")
    button = site.find_element('css', 'button')
    button.click()
    site.wait(10)
    site.select_window()
    button_1 = site.find_element('css', '#create-btn')
    button_1.click()
    site.wait(10)
    text = site.find_element('xpath', title_input)
    text.send_keys("Title123456")
    text = site.find_element('xpath', description)
    text.send_keys("Decription7895435677")
    text = site.find_element('xpath', content)
    text.send_keys("Content987654")
    button_2 = site.find_element('css', '.mdc-button__ripple')
    button_2.click()
    site.wait(10)
    site.select_window()
    title_output = '/html/body/div[1]/main/div/div[1]/h1'
    title_output = site.find_element('xpath', title_output)
    print(title_output.text)
    assert title_output == title_input


if __name__ == '__main__':
    pytest.main(['-v'])
