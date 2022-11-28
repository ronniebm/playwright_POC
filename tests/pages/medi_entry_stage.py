from playwright.sync_api import BrowserContext
from tests.environment import *
from tests import Locators


class EntryStage(Locators):

    def __init__(self, context: BrowserContext) -> None:
        super().__init__(context)
        self.PAGE = context.pages[0] if context.pages else context.new_page()
        self.URL = f'{ENV_URL}/medicaid/invoices/entry'

    def load(self) -> None:
        self.PAGE.goto("self.URL")

    def close(self) -> None:
        self.PAGE.context.pages[0].close()

    def click_new_invoice_btn(self) -> None:
        self.LOCATORS.entry_stage_medi_page.click_new_invoice_btn()

    def click_delete_invoice_btn(self) -> None:
        self.LOCATORS.entry_stage_medi_page.click_delete_invoice_btn()

    def click_export_btn(self) -> None:
        self.LOCATORS.entry_stage_medi_page.click_export_btn()
