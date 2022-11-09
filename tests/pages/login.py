from playwright.sync_api import Page, BrowserContext
from tests.environment import *


class LoginPage:

    def __init__(self, context: BrowserContext) -> None:
        self.PAGE = context.new_page()
        self.CLOSE_PAGE = context.pages[0]
        self.URL = f'{ENV_URL}/non-sso-login'

        # page locators.
        self.USERNAME_INPUT = self.PAGE.locator('input[name=username]')
        self.PASSWORD_INPUT = self.PAGE.locator('input[name=password]')
        self.SIGN_IN_BUTTON = self.PAGE.locator('button[type=submit]')

    def load(self) -> None:
        self.PAGE.goto(self.URL)

    def login(self, username: str, password: str) -> Page:
        self.USERNAME_INPUT.fill(username)
        self.PASSWORD_INPUT.fill(password)
        self.SIGN_IN_BUTTON.click()
        return self.PAGE
