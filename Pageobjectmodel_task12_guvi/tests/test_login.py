from pages.login_page import LoginPage
from selenium import webdriver

def test_valid_login_page():

    driver = webdriver.Chrome()

    driver.get("https://www.guvi.in")

    login = LoginPage(driver)

    login.enter_email_address_field("kishkaranptestengineer@gmail.com")
    login.enter_password_field("Kishore@123")
    login.click_login_button()

    assert "dashboard" in driver.current_url

    driver.quit()
