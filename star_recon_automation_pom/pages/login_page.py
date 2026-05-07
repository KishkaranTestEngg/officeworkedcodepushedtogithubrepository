class LoginPage:


    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://172.16.10.196:4200/auth/login")

    def login(self, username, password):
        self.page.get_by_role("textbox", name="Username").fill(username)
        self.page.get_by_role("textbox", name="Password").fill(password)

        self.page.locator("#pn_id_20_content").get_by_role("button").click()
        self.page.get_by_text("CGS").click()

        self.page.get_by_role("button", name="Login").click()