from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Dev\chromedriver.exe"
UPGRADES = 10
PRODUCTS = 18

driver= webdriver.Chrome(executable_path=chrome_driver_path)

event_x_path = '//*[@id="articlecount"]/a[1]'


driver.get("https://orteil.dashnet.org/cookieclicker/")

#articles = driver.find_element(By.XPATH, event_x_path)
#articles.click()


running = 1
while running:
    cookie = driver.find_element(By.ID, "bigCookie")
    for _ in range(0,500):
        try:
            cookie.click()
        except:
            pass

    for num in range(0, UPGRADES+1):

        try:
            upgrade = driver.find_element(By.ID, f"upgrade{UPGRADES-num}")
            upgrade.click()
        except:
            pass
    for num in range(0, PRODUCTS+1):

        try:
            upgrade = driver.find_element(By.ID, f"product{PRODUCTS-num}")
            upgrade.click()
        except:
            pass
