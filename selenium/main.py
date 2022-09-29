from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\Dev\chromedriver.exe"

driver= webdriver.Chrome(executable_path=chrome_driver_path)

event_x_path = '//*[@id="articlecount"]/a[1]'


driver.get("https://en.wikipedia.org/wiki/Main_Page")

articles = driver.find_element(By.XPATH, event_x_path).text

print(articles)

driver.quit()
