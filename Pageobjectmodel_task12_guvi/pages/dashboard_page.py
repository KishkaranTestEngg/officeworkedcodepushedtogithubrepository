from selenium.webdriver.common.by import By

class DashboardPage:

    logout = (By.ID, "logout")

    def __init__(self, driver):
        self.driver = driver

    def click_logout(self):
        self.driver.find_element(*self.logout).click()