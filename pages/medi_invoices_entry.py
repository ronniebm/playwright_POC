from playwright.sync_api import Page


class EntryPage:

    URL = 'https://qa-icyte-sparc.integrichain.net/medicaid/invoices/entry'

    def __init__(self, page: Page) -> None:
        self.PAGE = page
        self.NEW_INVOICE_BUTTON = page.locator('#invoice-new-btn')
        self.DELETE_INVOICE_BUTTON = page.locator('#invoice-delete-btn')
        self.EXPORT_BUTTON = page.locator('button[title=Export]')

    def load(self) -> None:
        self.PAGE.goto(self.URL)

    def create_new_invoice(self) -> None:
        self.NEW_INVOICE_BUTTON.click()