from selenium import webdriver

def get_driver():

    driver = webdriver.Chrome()

    driver.maximize_window()

    driver.get("https://www.guvi.in/sign-in/")

    return driver