from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element(By.NAME,value="fName" )
lname = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")
submit = driver.find_element(By.CLASS_NAME, value="btn")

fname.send_keys("Vedanth")
lname.send_keys("Lahoti")
email.send_keys("vedlahoti@gmail.com")
submit.click()

driver.quit()