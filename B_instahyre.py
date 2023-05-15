from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import TimeoutException

# Set up the ChromeOptions
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.binary_location = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe" # Replace with the actual path to Brave browser binary

# Set up the Chrome driver service
brave_path = "C:\\Users\\saque\\Downloads\\chromedriver_win32\\chromedriver.exe" # Replace with the actual path to Brave browser driver
service = ChromeService(executable_path=brave_path)

# Create the Chrome driver instance with Brave browser binary location and service
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://www.instahyre.com/login")
driver.maximize_window()

email = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
email.send_keys("<Your Email here>")

password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
password.send_keys("<Your Password here>")
password.send_keys(Keys.ENTER)

skills = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "skills-selectized")))
time.sleep(1)
skills.send_keys("software") # Any job filter you want to apply to.
skills.send_keys(Keys.ENTER)

# experience = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "years")))
# time.sleep(1)
# experience.send_keys("1")
# experience.send_keys(Keys.ENTER)

show_results = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "show-results")))
show_results.click()

view_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "interested-btn")))
view_button.click()

while True:
    try:
        apply = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-lg.btn-primary.new-btn")))
        print(apply.get_attribute("innerHTML"))

        apply.click()
        # WebDriverWait(driver, 10).until(EC.staleness_of(apply))
    except TimeoutException:
        print("No more companies to apply")
        break
