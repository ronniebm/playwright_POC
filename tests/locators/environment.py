from playwright.sync_api import BrowserContext
from tests.environment import *


# Locators for PAGE: Products.
# ---------------------------------------
class EnvironmentLocators:

    def __init__(self, context: BrowserContext) -> None:
        self.PAGE = context

    # ------------------------------
    # Click actions.
    def click_submit_btn(self):
        self.PAGE.pages[0].locator('text=Submit').click()

    # ------------------------------
    # [fill, set, select] actions.
    def select_client(self, value: str = CLIENT_AND_SERVICE[0]):
        self.PAGE.pages[0].locator('#client-selector').select_option(label=value)

    def select_service(self, value: str = CLIENT_AND_SERVICE[1]):
        self.PAGE.pages[0].locator('#service-selector').select_option(label=value)
