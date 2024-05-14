import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from constants import globalConstants

class TestInvalidLogins():
    def setup_method(self,method):
        self.driver = webdriver.Chrome()
        self.driver.get(globalConstants.url)
        self.driver.maximize_window()
        self.vars = {}

    def teardown_method(self,method):
        self.driver.quit()

    def read_data():
        with open("data.json","r") as file:
            data = json.load(file)
        return[(item["username"],item["password"],item["expected_error"])for item in data["invalid_log"]]
    
    @pytest.mark.parametrize("username,password,expected_error", read_data())
    def test_invalid_login1(self,username,password,expected_error):
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        self.driver.find_element(By.ID, globalConstants.login_button_id).click()
        error_message = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]")
        assert error_message.text == expected_error
        
    def test_invalid_login2(self):
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        username = self.driver.find_element(By.ID,"user-name")
        username.send_keys("standard_user")                  
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        self.driver.find_element(By.ID, globalConstants.login_button_id).click()
        assert self.driver.find_element (By.XPATH,"//*[@id=\"login_button_container\"]/div/form/div[3]/h3").text =="Epic sadface: Password is required"

    def test_invalid_login3(self):
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, globalConstants.username_id)))
        self.driver.find_element(By.ID, globalConstants.username_id).send_keys("locked_out_user")
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, globalConstants.password_id)))
        self.driver.find_element(By.ID, globalConstants.password_id).send_keys("secret_sauce")
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, globalConstants.login_button_id)))
        self.driver.find_element(By.ID, globalConstants.login_button_id).click()
        assert self.driver.find_element(By.XPATH, "//*[@id=\"login_button_container\"]/div/form/div[3]/h3").text == "Epic sadface: Sorry, this user has been locked out."


