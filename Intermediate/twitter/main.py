from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

TWITTER_EMAIL = "USER"
TWITTER_PASSWORD = "PASS"
PROMISED_DOWN = 755
PROMISED_UP = 100
chrome_driver_path = "C:\Dev\chromedriver.exe"

driver= webdriver.Chrome(executable_path=chrome_driver_path)


class InternetSpeedTwitterBot:
    def __init__(self, chrome_driver_path):
        self.driver= webdriver.Chrome(executable_path=chrome_driver_path)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        start = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        start.click()
        time.sleep(60)
        cross = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/a')
        cross.click()
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        print(f"Down: {self.down} Up: {self.up}")


    def tweet_at_provider(self):
        pass
        #twitter login and post

twitter_bot = InternetSpeedTwitterBot(chrome_driver_path)

#twitter_bot.get_internet_speed()
twitter_bot.tweet_at_provider()
