import re
from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(ignore_https_errors=True)
    page = context.new_page()
    page.goto("https://172.16.10.196:4200/auth/login")
    page.get_by_role("textbox", name="Username").fill("venkatdirect")
    page.get_by_role("textbox", name="Username").press("Tab")
    page.get_by_role("textbox", name="Password").fill("admin@123")
    page.get_by_role("textbox", name="Password").press("Tab")
    page.locator("#pn_id_21_content").get_by_role("button", name="dropdown trigger").click()
    page.get_by_role("option", name="CGS").click()
    page.get_by_role("button", name="Login").click()
    page.get_by_text("Checker - ATM & POS").click()
    page.get_by_text("Direct - ATM & POS").click()
    page.locator("a").filter(has_text=re.compile(r"^Configuration$")).click()
    page.locator("a").filter(has_text="Lookup Configuration").click()
    page.get_by_role("link", name="Card Type").click()
    page.get_by_role("button", name="Add").click()
    page.locator("#cardtypeFormId").get_by_role("button", name="dropdown trigger").click()
    page.get_by_label("CGS").get_by_text("CGS").click()
    page.get_by_role("textbox", name="Financial * Card Name * Card").click()
    page.get_by_role("textbox", name="Financial * Card Name * Card").fill("testingautomationaprillatest")
    page.get_by_role("textbox", name="Enter a Card No.").click()
    page.get_by_role("textbox", name="Enter a Card No.").fill("78")
    page.get_by_role("textbox", name="Financial * Card Name * Card").click()
    page.get_by_role("textbox", name="Financial * Card Name * Card").fill("testingautocheckaprillatest")
    page.get_by_role("textbox", name="Enter a Card No.").click()
    page.get_by_role("textbox", name="Enter a Card No.").fill("789456")
    page.get_by_role("textbox", name="Enter a Card Type").click()
    page.get_by_role("textbox", name="Enter a Card Type").fill("11")
    page.get_by_role("dialog").get_by_role("button", name="Add").click()
    page.get_by_role("button", name="Yes").click()
    page.get_by_role("textbox", name="Enter a Card Type").click()
    page.get_by_role("textbox", name="Enter a Card Type").fill("11")
    page.get_by_role("dialog").get_by_role("button", name="Add").click()
    page.locator("div").filter(has_text=re.compile(r"^Are you sure that you want to proceed with adding the new record\?$")).click()
    page.get_by_role("button", name="Yes").click()

    # ---------------------
    context.close()
    browser.close()


    # ---------------------
    context.close()
    browser.close()



with sync_playwright() as playwright:
    run(playwright)


