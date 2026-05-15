from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Launch Chrome browser
driver = webdriver.Chrome()

# Open GUVI website
driver.get("https://www.guvi.in")

# Maximize browser
driver.maximize_window()

# Wait for page loading
time.sleep(5)

# =========================
# Find "Practice" field
# =========================

practice = driver.find_element(By.XPATH, "//p[text()='Practice']")

# Mouse hover action
actions = ActionChains(driver)
actions.move_to_element(practice).perform()

time.sleep(3)

# =========================
# Parent Axis
# =========================

parent = practice.find_element(By.XPATH, "..")

print("The parent element value is:", parent.tag_name)

# =========================
# Child Axis
# =========================

children = parent.find_elements(By.XPATH, "./*")

for child in children:
    print("The child element values are:", child.tag_name)

# =========================
# Following-Sibling Axis
# =========================

following = practice.find_elements(By.XPATH, "following-sibling::*")

for f in following:
    print("The following sibling values are:", f.tag_name)

# =========================
# Preceding-Sibling Axis
# =========================

preceding = practice.find_elements(By.XPATH, "preceding-sibling::*")

for p in preceding:
    print("The preceding sibling values are:", p.tag_name)

# =========================
# Ancestor Axis
# =========================

ancestors = practice.find_elements(By.XPATH, "ancestor::*")

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

following_nodes = practice.find_elements(By.XPATH, "following::*")

for fn in following_nodes[:5]:
    print("The following node values are:", fn.tag_name)

# =========================
# Preceding Axis
# =========================

preceding_nodes = practice.find_elements(By.XPATH, "preceding::*")

for pn in preceding_nodes[-5:]:
    print("The preceding node values are:", pn.tag_name)

# =========================
# Self Axis
# =========================

self_node = practice.find_element(By.XPATH, "self::*")

print("The self node value is:", self_node.tag_name)

# Wait before closing
time.sleep(5)

# Close browser
driver.quit()