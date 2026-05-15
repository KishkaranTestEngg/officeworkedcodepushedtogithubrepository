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

# Find Login button
login = driver.find_element(By.XPATH, "//button[text()='Login']")

# =========================
# Parent Axis
# =========================

parent = login.find_element(By.XPATH, "..")

print("The parent element value is:", parent.tag_name)

# =========================
# Child Axis
# =========================

children = parent.find_elements(By.XPATH, "./*")

for child in children:
    print("The child element values are:", child.text)

# =========================
# Following-Sibling Axis
# =========================

following = login.find_elements(By.XPATH, "following-sibling::*")

for f in following:
    print("The following sibling values are:", f.text)

# =========================
# Preceding-Sibling Axis
# =========================

signup = driver.find_element(By.XPATH, "//button[text()='Sign up']")

preceding = signup.find_elements(By.XPATH, "preceding-sibling::*")

for p in preceding:
    print("The preceding sibling values are:", p.text)

# =========================
# Ancestor Axis
# =========================

ancestors = login.find_elements(By.XPATH, "ancestor::*")

for a in ancestors:
    print("The ancestor values are:", a.tag_name)

# =========================
# Descendant Axis
# =========================

descendants = parent.find_elements(By.XPATH, "descendant::*")

for d in descendants:
    print("The descendant values are:", d.tag_name)

# =========================
# Following Axis
# =========================

following_nodes = login.find_elements(By.XPATH, "following::*")

for fn in following_nodes[:5]:
    print("The following node values are:", fn.tag_name)

# =========================
# Preceding Axis
# =========================

preceding_nodes = signup.find_elements(By.XPATH, "preceding::*")

for pn in preceding_nodes[-5:]:
    print("The preceding node values are:", pn.tag_name)

# =========================
# Self Axis
# =========================

self_node = login.find_element(By.XPATH, "self::*")

print("The self node value is:", self_node.tag_name)

# Wait before closing
time.sleep(5)

# Close browser
driver.quit()