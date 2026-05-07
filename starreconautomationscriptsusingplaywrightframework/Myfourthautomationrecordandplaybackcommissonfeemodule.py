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
    page.locator("#pn_id_10").get_by_role("button", name="dropdown trigger").click()
    page.get_by_text("CGS").click()
    page.get_by_role("button", name="Login").click()
    page.locator("#pn_id_38").filter(has_text="Checker - ATM & POS").get_by_label("dropdown trigger").click()
    page.get_by_text("Direct - ATM & POS").click()
    page.locator("a").filter(has_text=re.compile(r"^Configuration$")).click()
    page.locator("a").filter(has_text="General Configuration").click()
    page.get_by_role("link", name="Commission Fee").click()
    page.get_by_role("button", name="Add").click()
    page.locator("p-dropdown").filter(has_text="Select a Financial").get_by_label("dropdown trigger").click()
    page.get_by_label("CGS").get_by_text("CGS").click()
    page.locator("p-dropdown").filter(has_text="Select a Network Name").get_by_label("dropdown trigger").click()
    page.get_by_role("option", name="NFS").click()
    page.get_by_role("textbox", name="Financial * Network Name *").click()
    page.get_by_role("textbox", name="Financial * Network Name *").fill("5000")
    page.get_by_role("textbox", name="Enter a To Amount").click()
    page.get_by_role("textbox", name="Enter a To Amount").fill("2000")
    page.get_by_role("textbox", name="Enter a From Rank").click()
    page.get_by_role("textbox", name="Enter a From Rank").fill("5")
    page.get_by_role("textbox", name="Enter a To Rank").click()
    page.get_by_role("textbox", name="Enter a To Rank").fill("2")
    page.locator("p-dropdown").filter(has_text="Select a Domestic/").get_by_label("dropdown trigger").click()
    page.get_by_text("Domestic", exact=True).click()
    page.get_by_role("textbox", name="Enter a Domestic Commission").click()
    page.get_by_role("textbox", name="Enter a Domestic Commission").fill("2500")
    page.get_by_role("textbox", name="Enter a Merchant Category Code").dblclick()
    page.get_by_role("textbox", name="Enter a Merchant Category Code").fill("458496")
    page.get_by_role("dialog").get_by_role("button", name="Add").click()
    page.get_by_role("button", name="Yes").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)


