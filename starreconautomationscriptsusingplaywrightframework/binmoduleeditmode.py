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
    page.locator("#pn_id_10").get_by_role("button", name="dropdown trigger").click()
    page.get_by_role("option", name="CGS").click()
    page.get_by_role("button", name="Login").click()
    page.locator("div").filter(has_text=re.compile(r"^Checker - ATM & POS$")).click()
    page.get_by_text("Direct - ATM & POS").click()
    page.locator("a").filter(has_text=re.compile(r"^Configuration$")).click()
    page.locator("a").filter(has_text="Source Configuration").click()
    page.locator("a").filter(has_text="Source Configuration").click()
    page.locator("a").filter(has_text="General Configuration").click()
    page.get_by_role("link", name="BIN").click()
    page.get_by_role("button", name="Edit").first.click()
    page.locator("#pn_id_304").get_by_role("button", name="dropdown trigger").click()
    page.get_by_role("option", name="NFS").click()
    page.get_by_role("textbox", name="Enter a Remarks").dblclick()
    page.get_by_role("textbox", name="Enter a Remarks").fill("testing in automationntesting edit mode")
    page.get_by_label("Edit BIN").get_by_role("button", name="Edit").click()
    page.get_by_text("NoYes").click()
    page.get_by_text("NoYes").click()
    page.get_by_role("button", name="Yes").click()
    page.get_by_role("button", name="Close").click()
    page.goto("https://172.16.10.196:4200/auth/login")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)


