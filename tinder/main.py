from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

logged_in = False
chrome_driver_path = "C:\Dev\chromedriver.exe"

driver= webdriver.Chrome(executable_path=chrome_driver_path)

login_xpath = '//*[@id="q-1470728188"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]'
FB_xpath = '//*[@id="q1095858032"]/main/div/div[1]/div/div/div[3]/span/div[2]/button'
password_xpath = '//*[@id="pass"]'
user_xpath = '//*[@id="email"]'
location_xpath = '//*[@id="q1095858032"]/main/div/div/div/div[3]/button[1]'
cookies_xpath = '//*[@id="q-1470728188"]/div/div[2]/div/div/div[1]/div[2]/button'
notifications_xpath = '//*[@id="q1095858032"]/main/div/div/div/div[3]/button[1]'
later_xpath = '//*[@id="q1095858032"]/main/div/div/div[3]/button[2]'
like_button_xpath = '//*[@id="q-1470728188"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[2]/div/div/div[4]/button'
cross_xpath = '//*[@id="q-1140356987"]/main/div/div[1]/div/div[4]/button'


driver.get("https://tinder.com/")

time.sleep(2)
login = driver.find_element(By.XPATH, login_xpath)
login.click()
time.sleep(2)
fb = driver.find_element(By.XPATH, FB_xpath)
fb.click()
time.sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

username = driver.find_element(By.XPATH, user_xpath)
username.send_keys("USER")
password = driver.find_element(By.XPATH, password_xpath)
password.send_keys("PASS")
password.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)

time.sleep(5)
location = driver.find_element(By.XPATH, location_xpath)
location.click()
time.sleep(1)
cookies = driver.find_element(By.XPATH, cookies_xpath)
cookies.click()
time.sleep(1)
notifications = driver.find_element(By.XPATH, notifications_xpath)
notifications.click()
time.sleep(1)
later = driver.find_element(By.XPATH, later_xpath)
later.click()



def like():
    try:
        like_button = driver.find_element(By.XPATH, like_button_xpath)
        like_button.click()
        time.sleep(2)
    except:
        cross = driver.find_element(By.XPATH, cross_xpath)
        cross.click()
        time.sleep(1)
    finally:
        like()

time.sleep(2)
like()
