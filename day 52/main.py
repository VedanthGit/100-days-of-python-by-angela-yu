import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
import dotenv

dotenv.load_dotenv()

SIMILAR_ACCOUNT = "Instagram"
USERNAME = os.getenv("YOUR_INSTAGRAM_EMAIL")
PASSWORD = os.getenv("YOUR_INSTAGRAM_PASSWORD")

class InstaFollower:

    def __init__(self):
        # Optional - Keep browser open (helps diagnose issues during a crash)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=chrome_options)
        

    def login(self):
        url = "https://www.instagram.com/accounts/login/"
        self.driver.get(url)
        
        wait = WebDriverWait(self.driver, 15)   
        
        email = wait.until(EC.presence_of_element_located((By.NAME, "email")))

        password = wait.until(EC.presence_of_element_located((By.NAME, "pass")))
        
        email.send_keys(USERNAME)
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)
        
        not_now_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='button' and text()='Not now']")))
        if not_now_btn:
            not_now_btn.click()
        
    def find_followers(self):
        
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")
        wait = WebDriverWait(self.driver, 20)
        
        modal = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='dialog']//div[contains(@style, 'overflow')]")))
        for i in range(10):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as an HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(1.2)

    def follow(self):
        wait = WebDriverWait(self.driver, 20)
        all_buttons = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '._aano button')))

        for button in all_buttons:
            try:
                button.click()
                sleep(1.1)
            # Clicking button for someone who is already being followed will trigger dialog to Unfollow/Cancel
            except ElementClickInterceptedException:
                cancel_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Cancel')]")))
                cancel_button.click()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
