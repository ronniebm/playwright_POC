from playwright.sync_api import Page, BrowserContext
from tests.locators.products import ProductLocators, ModalAddProductLocators
from tests.locators.environment import EnvironmentLocators
from tests.locators.login import LoginLocators
from tests.locators.medi_entry_stage import EntryStageMediLocators


# --------------------------------------------------
# LocatorCollector class.
# - attributes can be added for every page.
# --------------------------------------------------
class LocatorCollector:

    def __init__(self, context: BrowserContext) -> None:
        self.products_page = ProductLocators(context)
        self.login_page = LoginLocators(context)
        self.environment_page = EnvironmentLocators(context)
        self.entry_stage_medi_page = EntryStageMediLocators(context)


# --------------------------------------------------
# Locators CLASS - * DONT MODIFY UNLESS NECCESARY *.
# --------------------------------------------------
class Locators:

    def __init__(self, context: BrowserContext) -> None:
        self.LOCATORS = LocatorCollector(context)
