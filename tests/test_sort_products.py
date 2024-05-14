import pytest
import openpyxl
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


class TestSortProduduct():
    def setup_method(self,method):
        self.driver = webdriver.Chrome()
        self.driver.get(globalConstants.url)
        self.driver.maximize_window()
        self.vars = {}

    def teardown_method(self,method):
        self.driver.quit()

    def test_sort_product(self):
        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameInput.send_keys("standard_user")
        passwordInput =WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput.send_keys("secret_sauce")
        loginButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        loginButton.click()
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='header_container']/div[2]/div/span/select/option[3]")))
        sortingList = self.driver.find_element(By.XPATH,"//*[@id=\"header_container\"]/div[2]/div/span/select/option[3]")
        sortingList.click()
        firstTwoProductPrices = self.driver.find_elements(By.XPATH, "//div[@class='inventory_item_price']")
        firstTwoProductPrices = [float(element.text.replace("$", "")) for element in firstTwoProductPrices]
        assert firstTwoProductPrices[0] <= firstTwoProductPrices[1]
         

   