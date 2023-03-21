from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

class Test_Kodlamaio:
    def test_invalid_login(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        inputUser = driver.find_element(By.ID,"user-name")
        inputPass = driver.find_element(By.ID,"password")
        inputUser.send_keys("1")
        inputPass.send_keys("2")
        loginBtn = driver.find_element(By.ID,"login-button")
        loginBtn.click()
        errorMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
        print(f"Test SONUCU : {testResult}")
        

testClass = Test_Kodlamaio()
testClass.test_invalid_login()
