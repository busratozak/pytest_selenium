import pytest
import openpyxl
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from constants import globalConstants 
from time import sleep

class TestLogout():
    
    def setup_method(self,method):
        self.driver = webdriver.Chrome()
        self.driver.get(globalConstants.url)
        self.driver.maximize_window()
        self.vars = {}

    def teardown_method(self,method):
        self.driver.quit()

    @pytest.mark.skip
    def test_logout(self):
        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameInput.send_keys("standard_user")
        passwordInput =WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput.send_keys("secret_sauce")
        loginButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        loginButton.click()
        menuButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"react-burger-menu-btn")))
        menuButton.click()
        logoutButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"logout_sidebar_link")))
        logoutButton.click()
        assert self.driver.current_url == globalConstants.url
