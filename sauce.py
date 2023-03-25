from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains

class Test_Kodlamaio:
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())   
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
    
    def test_invalid_login(self):
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        inputUser = self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        inputPass = self.driver.find_element(By.ID,"password")
        inputUser.send_keys("1")
        inputPass.send_keys("2")
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
        print(f"Test SONUCU : {testResult}")
    def test_valid_login(self):
        self.driver.get("https://www.saucedemo.com/")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        inputUser = self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        inputPass = self.driver.find_element(By.ID,"password")
        # Action Chains
        actions = ActionChains(self.driver) 
        actions.send_keys_to_element(inputUser,"standard_user")   
        actions.send_keys_to_element(inputPass,"secret_sauce")   
        actions.perform()
        #inputUser.send_keys("standard_user")
        #inputPass.send_keys("secret_sauce")
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        self.driver.execute_script("window.scrollTo(0,500)")
      
        



testClass = Test_Kodlamaio()
testClass.test_invalid_login()
testClass.test_valid_login()