from playwright.sync_api import BrowserContext
from tests.environment import *


# Locators for PAGE: Entry Stage (medi workflow).
# -----------------------------------------------
class EntryStageMediLocators:

    def __init__(self, context: BrowserContext) -> None:
        self.PAGE = context

    # ------------------------------
    # Click actions.
    def click_new_invoice_btn(self):
        self.PAGE.pages[0].locator('#invoice-new-btn').click()

    def click_delete_invoice_btn(self):
        self.PAGE.pages[0].locator('#invoice-delete-btn').click()

    def click_export_btn(self):
        self.PAGE.pages[0].locator('button[title=Export]').click()

    # ------------------------------
    # [fill, set, select] actions.
