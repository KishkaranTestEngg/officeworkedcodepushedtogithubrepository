from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
import time

# Launch browser
driver = webdriver.Chrome()

# Open website
driver.get("https://jqueryui.com/droppable/")

# Maximize browser window
driver.maximize_window()

# Switch to iframe
frame = driver.find_element(By.CLASS_NAME, "demo-frame")
driver.switch_to.frame(frame)

# Locate draggable and droppable elements
source = driver.find_element(By.ID, "draggable")
target = driver.find_element(By.ID, "droppable")

# # Perform drag and drop
actions = ActionChains(driver)
actions.drag_and_drop(source, target).perform()

# Wait for 3 seconds
time.sleep(3)

print("Drag and Drop successful")

# Close browser
driver.quit()