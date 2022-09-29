from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Dev\chromedriver.exe"

driver= webdriver.Chrome(executable_path=chrome_driver_path)

event_x_path = '//*[@id="articlecount"]/a[1]'


driver.get("http://secure-retreat-92358.herokuapp.com/")

#articles = driver.find_element(By.XPATH, event_x_path)
#articles.click()

search = driver.find_element(By.NAME, "fName")
search.send_keys("Bob")
search = driver.find_element(By.NAME, "lName")
search.send_keys("Bobington")
search = driver.find_element(By.NAME, "email")
search.send_keys("Bob@Bobington.com")
search.send_keys(Keys.ENTER)
