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
    page.get_by_text("CGS").click()
    page.get_by_role("button", name="Login").click()
    page.locator("#pn_id_38").get_by_role("button", name="dropdown trigger").click()  # new code change after the angular fix.
    page.get_by_text("Direct - ATM & POS").click()
    page.locator("a").filter(has_text=re.compile(r"^Configuration$")).click()
    page.locator("a").filter(has_text="General Configuration").click()
    page.get_by_role("link", name="BIN").click()
    page.locator("div").filter(has_text=re.compile(r"^Add$")).first.click()
    page.get_by_role("button", name="Add").click()
    page.locator("#pn_id_311").filter(has_text="Select a Financial").get_by_label("dropdown trigger").click()  # Finding the issue after the angular update line no 23
    page.get_by_role("option", name="CGS").click()
    page.get_by_text("Select an Entity").click()
    page.get_by_role("option", name="VISA").click()
    page.get_by_role("textbox", name="Financial * Entity * BIN No").click()
    page.get_by_role("textbox", name="Financial * Entity * BIN No").click()
    page.get_by_role("textbox", name="Financial * Entity * BIN No").fill("451256")
    page.locator("#pn_id_313").filter(has_text="Select a Card Type").get_by_label("dropdown trigger").click()
    page.get_by_role("option", name="TEST", exact=True).click()
    page.get_by_role("textbox", name="Enter a Remarks").click()
    page.get_by_role("textbox", name="Enter a Remarks").fill("testing bin module in automation scripts")
    page.get_by_role("dialog").get_by_role("button", name="Add").click()
    page.get_by_role("button", name="Yes").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)



