import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

TINDER_URL = "https://tinder.com/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
driver.get(TINDER_URL)

wait = WebDriverWait(driver, 20)

driver.get(TINDER_URL)


login_button = wait.until(ec.element_to_be_clickable((By.XPATH,"//a[contains(text(),'Log in')]")))
login_button.click()

options_button = wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="q-1018673301"]/div/div[1]/div/div[2]/div/div/div[2]/div[2]/span/button')))
options_button.click()

fb_login = wait.until(
    ec.element_to_be_clickable((
            By.XPATH,
            '//*[@id="q-1018673301"]/div/div[1]/div/div[2]/div/div/div[2]/div[2]/span/div[2]/button'
    ))
)
fb_login.click()

base_window = driver.current_window_handle

wait.until(ec.number_of_windows_to_be(2))

for window in driver.window_handles:
    if window != base_window:
        driver.switch_to.window(window)
        break
    
# driver.switch_to.window(fb_window)
print("Facebook Window Title: ",driver.title)

wait.until(ec.number_of_windows_to_be(1))

driver.switch_to.window(base_window)
print("Back to Tinder: ",driver.title)

try:
    for iframe in driver.find_elements(By.TAG_NAME, "iframe"):
        driver.switch_to.frame(iframe)
        break
except:
    pass

try:
    continue_btn = wait.until(
        ec.element_to_be_clickable((
            By.XPATH,
            "//*[contains(text(),'Continue')]"
        ))
    )
    continue_btn.click()
except:
    print("No Continue button — auto-login successful.")

driver.switch_to.default_content()

print("✅ Login flow finished successfully.")

# Tinder Handle
for n in range(100):
    sleep(1)
    
    try:
        print("called")
        like_button = ec.element_to_be_clickable((By.XPATH, '//*[@id="main-content"]/div[1]/div/div/div/div[1]/div/div/div[4]/div/div[2]/button'))
        like_button.click()
        
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            sleep(2)
            
driver.quit()