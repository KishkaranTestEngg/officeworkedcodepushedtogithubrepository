
from pages.login_page import LoginPage


def test_full_star_recon_application_flow(page):

    login_page = LoginPage(page)

    login_page.navigate()
    login_page.login("venkatdirect", "admin@123")