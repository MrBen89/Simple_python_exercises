from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\Dev\chromedriver.exe"

driver= webdriver.Chrome(executable_path=chrome_driver_path)

event_x_path = '//*[@id="content"]/div/section/div[2]/div[2]/div/ul'


driver.get("https://www.python.org/")

dates = []
events = []
dic = {}
for num in range(1,6):
    date = driver.find_element(By.XPATH, f"{event_x_path}/li[{num}]/time").text
    event = driver.find_element(By.XPATH, f"{event_x_path}/li[{num}]/a").text
    dic[len(dic)] = {"time": date, "name": event}

print(dic)

driver.quit()
