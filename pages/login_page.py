class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username = page.locator("#user-name")
        self.password = page.locator("#password")
        self.login_btn = page.locator("#login-button")

    def goto(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self, user, pwd):
        self.username.fill(user)
        self.password.fill(pwd)
        self.login_btn.click()