import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected

load_dotenv()

browser = webdriver.Chrome()
url = 'https://www.hudl.com/login'
pass_url = 'https://www.hudl.com/home'
fail_url = 'https://www.hudl.com/login'

test_pass = os.getenv('PASSWORD')
test_email = os.getenv('USERNAME')

# Tests for proper result when Login button is clicked
def test_click_button(name,password,expectedurl):
    browser.get(url)
    email_input = browser.find_element_by_id('email')
    password_input = browser.find_element_by_id('password')
    login_button = browser.find_element_by_id('logIn')
    email_input.send_keys(name)
    password_input.send_keys(password)
    login_button.click()
    WebDriverWait(browser, 7).until(expected.url_to_be(expectedurl))
    assert browser.title == expectedurl

# Tests for proper result when enter key is typed
def test_enter(name,password,expectedurl):
    browser.get(url)
    email_input = browser.find_element_by_id('email')
    password_input = browser.find_element_by_id('password')
    email_input.send_keys(name)
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)
    WebDriverWait(browser, 7).until(expected.url_to_be(expectedurl))
    assert browser.title == expectedurl

#Test Function Call:
test_click_button(test_email,test_pass,pass_url)
test_click_button(test_email,'Blue237!',fail_url)
test_click_button('gary123@gmail.com',test_pass,fail_url)
#Pass
test_enter(test_email,test_pass,pass_url)
test_enter(test_email,'Yellow1!',fail_url)
test_enter('tim123@yahoo.com',test_pass,fail_url)
#Pass