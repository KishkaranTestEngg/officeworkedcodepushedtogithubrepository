from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch Chrome browser
driver = webdriver.Chrome()

# Open GUVI website
driver.get("https://www.guvi.in")

# Maximize browser
driver.maximize_window()

# Wait for page loading
time.sleep(5)

# Find Sign up button
signup = driver.find_element(By.XPATH, "//button[text()='Sign up']")

# Find parent element
parent = signup.find_element(By.XPATH, "..")

# Print parent tag
print(parent.tag_name)

time.sleep(5)

driver.quit()