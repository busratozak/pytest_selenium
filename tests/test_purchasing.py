import pytest
import openpyxl
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from constants import globalConstants 
from time import sleep

class TestPurchasing():
    
    def setup_method(self,method):
        self.driver = webdriver.Chrome()
        self.driver.get(globalConstants.url)
        self.driver.maximize_window()
        self.vars = {}

    def teardown_method(self,method):
        self.driver.quit()

    def test_purchasing(self):
        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameInput.send_keys("standard_user")
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput.send_keys("secret_sauce")
        loginButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        loginButton.click()
        addToCard = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CSS_SELECTOR,"#add-to-cart-sauce-labs-bike-light")))
        addToCard.click()
        shoppingCard = WebDriverWait (self.driver,5).until(ec.visibility_of_element_located((By.CLASS_NAME,"shopping_cart_link")))
        shoppingCard.click()
        checkout = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"checkout")))
        checkout.click()
        firstName = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"first-name")))
        firstName.send_keys("Büşra")
        lastName = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"last-name")))
        lastName.send_keys("Tozak")
        postalCode = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"postal-code")))
        postalCode.send_keys("3434")
        self.driver.execute_script("window.scrollTo(0, 500);")
        continueButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"continue")))
        continueButton.click()
        finishButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id=\"finish\"]")))
        finishButton.click()
        completeText = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CLASS_NAME,"complete-text")))
        assert completeText.text == "Your order has been dispatched, and will arrive just as fast as the pony can get there!"

