from playwright.sync_api import Page, BrowserContext
from tests.locators.products import ProductLocators, AddProductModalLocators


class LocatorCollector:

    def __init__(self, context: BrowserContext) -> None:
        self.products_page = ProductLocators(context)


class Locators:

    def __init__(self, context: BrowserContext) -> None:
        self.LOCATORS = LocatorCollector(context)
