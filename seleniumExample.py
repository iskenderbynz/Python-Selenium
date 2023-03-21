from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.google.com/")
input =driver.find_element(By.NAME,"q")
input.send_keys("kodlamaio")
searchButton = driver.find_element(By.NAME,"btnK")
sleep(1)
searchButton.click()
sleep(1)
firstResult = driver.find_element(By.XPATH,"/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/a")
sleep(1)
firstResult.click()
sleep(1)
listOfCourses = driver.find_elements(By.CLASS_NAME,"course-listing")

print(f"Kodlamaio sitesinde suanda {len(listOfCourses)} adet kurs var")

#/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/a
#sleep(10)
while True:
    continue
