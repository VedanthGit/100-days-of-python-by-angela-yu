import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import dotenv

dotenv.load_dotenv()

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = os.getenv("YOUR_TWITTER_EMAIL")
TWITTER_PASSWORD = os.getenv("YOUR_TWITTER_PASSWORD")
TWITTER_PHONE_NUMBER = os.getenv("YOUR_PHONE_NUMBER")


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 20)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        
        sleep(3)

        go_button = self.wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[2]/a')))
        go_button.click()

        self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "span.download-speed")))
        
        
        self.up = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.down = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text


    def tweet_at_provider(self):
        # sleep(60)
        self.driver.get("https://twitter.com/login")

        email = self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, '#layers > div > div > div > div > div > div > div.css-175oi2r.r-1ny4l3l.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv.r-1awozwy > div.css-175oi2r.r-1wbh5a2.r-htvplk.r-1udh08x.r-1867qdf.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1 > div > div > div.css-175oi2r.r-1ny4l3l.r-6koalj.r-16y2uox.r-kemksi.r-1wbh5a2 > div.css-175oi2r.r-16y2uox.r-1wbh5a2.r-f8sm7e.r-13qz1uu.r-1ye8kvj > div > div > div > div.css-175oi2r.r-1mmae3n.r-1e084wi.r-13qz1uu > label > div > div.css-175oi2r.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-xd6kpl.r-is05cd.r-ttdzmv > div > input')))
        # email.click()
        email.send_keys(TWITTER_EMAIL)
        # email.send_keys(Keys.ENTER)
        
        next_button = self.wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]')))
        
        next_button.click()
        
        phone_number = self.wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')))
        
        phone_number.send_key(TWITTER_PHONE_NUMBER)
        phone_number.send_keys(Keys.ENTER)
        
        password = self.wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')))
        # password.click()
        password.send_keys(TWITTER_PASSWORD)
        sleep(2)
        password.send_keys(Keys.ENTER)

        sleep(5)
        tweet_compose = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')

        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        sleep(3)

        tweet_button = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()

        sleep(2)
        self.driver.quit()
    
bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()