from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

class Test_Kodlamaio:
    def login_control1(self):  
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()    
        driver.get("https://www.saucedemo.com/")
        loginBtn = driver.find_element(By.ID,"login-button")
        loginBtn.click()
        errorMessage = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Username is required"
        print(f"Senaryo 1 Test Sonucu : {testResult}")
        driver.close()
        menu()

    def login_control2(self):
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver.maximize_window()
            driver.get("https://www.saucedemo.com/")
            inputUser = driver.find_element(By.ID,"user-name")
            inputPass = driver.find_element(By.ID,"password")
            inputUser.send_keys("standard_user")
            inputPass.send_keys("")
            loginBtn = driver.find_element(By.ID,"login-button")
            loginBtn.click()
            errorMessage = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
            testResult = errorMessage.text == "Epic sadface: Password is required"
            print(f"Senaryo 2 Test Sonucu : {testResult}")
            driver.close()
            menu()
    
    def login_control3(self):
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver.maximize_window()
            driver.get("https://www.saucedemo.com/")
            inputUser = driver.find_element(By.ID,"user-name")
            inputPass = driver.find_element(By.ID,"password")
            inputUser.send_keys("locked_out_user")
            inputPass.send_keys("secret_sauce")
            loginBtn = driver.find_element(By.ID,"login-button")
            loginBtn.click()
            errorMessage = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
            testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
            print(f"Senaryo 3 Test Sonucu : {testResult}")
            driver.close()
            menu()

    def login_control4(self):
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver.maximize_window()
            driver.get("https://www.saucedemo.com/")
            inputUser = driver.find_element(By.ID,"user-name")
            inputPass = driver.find_element(By.ID,"password")
            inputUser.send_keys("")
            inputPass.send_keys("")
            loginBtn = driver.find_element(By.ID,"login-button")
            loginBtn.click()
            inputIcon = driver.find_elements(By.XPATH,"//*[name()='svg']")
            if len(inputIcon) == 3:
                errorMessageClose = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button")
                errorMessageClose.click()
                inputIcon = driver.find_elements(By.XPATH,"//*[name()='svg']")
            
            testResult = len(inputIcon) == 0
            print(f"Senaryo 4 Test Sonucu : {testResult}")
            driver.close()
            menu()

    def login_control5(self):
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver.maximize_window()
            driver.get("https://www.saucedemo.com/")
            inputUser = driver.find_element(By.ID,"user-name")
            inputPass = driver.find_element(By.ID,"password")
            inputUser.send_keys("standard_user")
            inputPass.send_keys("secret_sauce")
            loginBtn = driver.find_element(By.ID,"login-button")
            loginBtn.click()
            pageActive = driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[2]/span")
            pageTitle = pageActive.text == "Products"
            print(f"Senaryo 5 Test Sonucu : {pageTitle}")
            driver.close()
            menu()

    def login_control6(self):
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver.maximize_window()
            driver.get("https://www.saucedemo.com/")
            inputUser = driver.find_element(By.ID,"user-name")
            inputPass = driver.find_element(By.ID,"password")
            inputUser.send_keys("standard_user")
            inputPass.send_keys("secret_sauce")
            loginBtn = driver.find_element(By.ID,"login-button")
            loginBtn.click()
            productCount = driver.find_elements(By.CLASS_NAME,"inventory_item_name")
            testResult = len(productCount) == 6
            print(f"Senaryo 6 Test Sonucu : {testResult}")
            driver.close()
            menu()
            

testClass = Test_Kodlamaio()

def menu():
      print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
      print("1 - Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak 'Epic sadface: Username is required' gösterilmelidir.")
      print("2 - Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak 'Epic sadface: Password is required' gösterilmelidir.")
      print("3 - Kullanıcı adı 'locked_out_user' şifre alanı 'secret_sauce' gönderildiğinde 'Epic sadface: Sorry, this user has been locked out.' mesajı gösterilmelidir.")
      print("4 - Kullanıcı adı ve şifre alanları boş geçildiğinde bu iki inputun yanında da kırmızı 'X' ikonu çıkmalıdır. Daha sonra aşağıda çıkan uyarı mesajının kapatma butonuna tıklandığında bu 'X' ikonları kaybolmalıdır.")
      print("5 - Kullanıcı adı 'standard_user' şifre 'secret_sauce' gönderildiğinde kullanıcı '/inventory.html' sayfasına gönderilmelidir.")
      print("6 - Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı '6' adet olmalıdır.")
      print("7 - Çıkış Yap")
      print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
      menuSec = input("Testini başlatmak istediğiniz senaryoyu seçiniz : ")
      if menuSec=="1":
            testClass.login_control1()
      if menuSec=="2":
            testClass.login_control2()
      if menuSec=="3":
            testClass.login_control3()
      if menuSec=="4":
            testClass.login_control4()
      if menuSec=="5":
            testClass.login_control5()
      if menuSec=="6":
            testClass.login_control6()
      if menuSec=="7":
            quit()
menu()