from playwright.sync_api import BrowserContext
from tests.environment import *


# Locators for PAGE: Products.
# ---------------------------------------
class LoginLocators:

    def __init__(self, context: BrowserContext) -> None:
        self.PAGE = context

    # ------------------------------
    # Click actions.
    def click_sign_in_btn(self):
        self.PAGE.pages[0].locator('button[type=submit]').click()

    # ------------------------------
    # [fill, set, select] actions.
    def fill_username(self, value: str = ANALYST_CREDENTIALS[0]):
        self.PAGE.pages[0].locator('input[name=username]').fill(value)

    def fill_password(self, value: str = ANALYST_CREDENTIALS[1]):
        self.PAGE.pages[0].locator('input[name=password]').fill(value)
