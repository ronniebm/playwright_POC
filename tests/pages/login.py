from playwright.sync_api import Page


class LoginPage:

    URL = 'https://qa-icyte-sparc.integrichain.net/non-sso-login'

    def __init__(self, page: Page) -> None:
        self.PAGE = page
        self.USERNAME_INPUT = page.locator('input[name=username]')
        self.PASSWORD_INPUT = page.locator('input[name=password]')
        self.SIGN_IN_BUTTON = page.locator('button[type=submit]')

    def load(self) -> None:
        self.PAGE.goto(self.URL)

    def login(self, username: str, password: str) -> Page:
        self.USERNAME_INPUT.fill(username)
        self.PASSWORD_INPUT.fill(password)
        self.SIGN_IN_BUTTON.click()
        return self.PAGE
