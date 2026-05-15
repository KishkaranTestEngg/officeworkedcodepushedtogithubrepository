from selenium.webdriver.common.by import By

class LoginPage:

    email_address_field = (By.XPATH, "//input[@id='email']")
    password_field = (By.XPATH, "//input[@id='password']")
    login_button = (By.XPATH, "//*[@id='login-btn']")

    def __init__(self, driver):
        self.driver = driver

    def enter_email_address_field(self, username):
        self.driver.find_element(*self.email_address_field).send_keys(username)

    def enter_password_field(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()