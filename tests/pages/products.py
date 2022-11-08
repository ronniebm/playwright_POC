from playwright.sync_api import Page, BrowserContext
from tests.environment_vars import *


class ProductsPage:

    URL = f'{ENV_URL}/masterdata/products'

    def __init__(self, context: BrowserContext) -> None:
        self.PAGE = context.new_page()

    def load(self) -> None:
        self.PAGE.goto(self.URL)


