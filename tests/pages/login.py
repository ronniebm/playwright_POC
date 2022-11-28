from playwright.sync_api import BrowserContext
from tests.environment import *
from tests import Locators


class LoginPage(Locators):

    def __init__(self, context: BrowserContext) -> None:
        super().__init__(context)
        self.PAGE = context.pages[0] if context.pages else context.new_page()
        self.URL = f'{ENV_URL}/non-sso-login'

    def load(self) -> None:
        self.PAGE.goto(self.URL)

    def close(self) -> None:
        self.PAGE.context.pages[0].close()

    def fill_login_credentials(self) -> None:
        self.LOCATORS.login_page.fill_username()
        self.LOCATORS.login_page.fill_password()

    def click_sign_in_btn(self) -> BrowserContext:
        self.LOCATORS.login_page.click_sign_in_btn()
        return self.PAGE.context
