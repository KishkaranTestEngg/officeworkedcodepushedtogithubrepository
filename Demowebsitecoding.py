
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class LoginFunctionality:

    def __init__(self, driver):
        self.driver = driver

    def check_url(self):
        expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        if self.driver.current_url == expected_url:
            print("URL correct")
        else:
            print("URL Failed")

    def check_title(self):
        expected_title = "OrangeHRM"
        if self.driver.title == expected_title:
            print("Title Successful")
        else:
            print("Title Failed")

    def check_username(self):
        username = self.driver.find_element(By.NAME, "username")
        if username.is_displayed():
            print("Username field is displayed")
        else:
            print("Username field not displayed")

    def check_password(self):
        password = self.driver.find_element(By.NAME, "password")
        if password.is_displayed():
            print("Password field is displayed")
        else:
            print("Password field not displayed")

    def check_button(self):
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        if login_button.is_enabled():
            print("Login button is enabled")
        else:
            print("Login button is not enabled")


# -------- Main Execution --------
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(3)

login = LoginFunctionality(driver)
login.check_url()
login.check_title()
login.check_username()
login.check_password()
login.check_button()

driver.quit()
