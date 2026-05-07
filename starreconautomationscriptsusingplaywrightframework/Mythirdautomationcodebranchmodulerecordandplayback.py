import re
from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(ignore_https_errors=True)
    page = context.new_page()
    page.goto("https://172.16.10.196:4200/auth/login")
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("venkatdirect")
    page.get_by_role("textbox", name="Username").press("Tab")
    page.get_by_role("textbox", name="Password").fill("admin@123")
    page.locator("#pn_id_10").get_by_role("button", name="dropdown trigger").click() # After the angular change worked code
    page.get_by_role("option", name="CGS").click()
    page.get_by_role("button", name="Login").click()
    page.locator("#pn_id_38").filter(has_text="Checker - ATM & POS").get_by_label("dropdown trigger").click() # After the angular change worked code
    page.get_by_text("Direct - ATM & POS").click()
    page.locator("a").filter(has_text=re.compile(r"^Configuration$")).click()
    page.locator("a").filter(has_text="General Configuration").click()
    page.get_by_role("link", name="Branch").click()
    page.get_by_role("button", name="Add").click()
    page.locator("#pn_id_293").filter(has_text="Select a Financial").get_by_label("dropdown trigger").click() # changes made after the angular update in financial drop-down
    page.get_by_role("option", name="RECON").click()
    page.locator("#pn_id_294").filter(has_text="Select an District Name").get_by_label("dropdown trigger").click() # changes made after the angular update in select district drop-down
    page.get_by_role("option", name="TestNameD").click()
    page.get_by_role("textbox", name="Financial * District Name *").click()
    page.get_by_role("textbox", name="Financial * District Name *").fill("7989889899")
    page.get_by_role("textbox", name="Financial * District Name *").press("Tab")
    page.get_by_role("textbox", name="Enter a Branch Name").fill("testbranchnamejkekkkevkvkvdsvvnkvenkata")
    page.get_by_role("textbox", name="Enter a Branch Name").press("Tab")
    page.get_by_role("textbox", name="Enter a Contact No.").fill("798989898989898")
    page.get_by_role("textbox", name="Enter a Contact No.").press("Tab")
    page.get_by_role("textbox", name="Enter an Address").fill("testthebranchcodewiththefollowoingserviceofautomationtesting")
    page.get_by_role("dialog").get_by_role("button", name="Add").click()
    page.get_by_role("button", name="Yes").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
