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
print("The parent element value are",parent.tag_name)


# Find the child element

children = parent.find_elements(By.XPATH, "./*")

for child in children:
    print("The child element values are",child.text)

# Find in the sibling level

login = driver.find_element(By.XPATH, "//button[text()='Login']")

following = login.find_elements(By.XPATH, "following-sibling::*")

for f in following:
    print('The sibling element values are',f.text)

# find using the Preceding Sibling

previous = signup.find_elements(By.XPATH, "preceding-sibling::*")

for p in previous:
    print('The preceding sibling values are',p.text)

# find using the Ancestor axis

ancestors = signup.find_elements(By.XPATH, "ancestor::*")

for a in ancestors:
    print("The ancestor sibling value are",a.tag_name)

# Find using the Descendant axis

descendants = parent.find_elements(By.XPATH, "descendant::*")

for d in descendants:
    print("The descendant sibling value are",d.tag_name)

time.sleep(5)

driver.quit()