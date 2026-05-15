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
    page.get_by_role("option", name="CGS").click()
    page.get_by_role("button", name="Login").click()
    page.locator("#pn_id_38").get_by_role("button", name="dropdown trigger").click()
    page.get_by_text("Direct - ATM & POS").click()
    page.locator("a").filter(has_text=re.compile(r"^Configuration$")).click()
    page.locator("a").filter(has_text="General Configuration").click()
    page.get_by_role("link", name="Branch").click()
    page.get_by_role("button", name="Edit").first.click()
    page.locator("#pn_id_293").get_by_role("button", name="dropdown trigger").click()
    page.get_by_role("textbox", name="Enter a Contact No.").dblclick()
    page.get_by_role("textbox", name="Enter a Contact No.").fill("549595956556")
    page.get_by_role("textbox", name="Enter an Address").click()
    page.get_by_role("textbox", name="Enter an Address").fill("chennai edit done in branch mode")
    page.get_by_text("CancelEdit").click()
    page.get_by_label("Edit Branch").get_by_role("button", name="Edit").click()
    page.get_by_role("button", name="Yes").click()
    page.get_by_label("Edit Branch").get_by_role("button", name="Edit").click()
    page.get_by_role("button", name="Yes").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)