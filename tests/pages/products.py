from playwright.sync_api import Page
from tests.environment_vars import *


class ProductsPage:

    URL = f'{ENV_URL}/masterdata/products'

    def __init__(self, page: Page) -> None:
        self.PAGE = page

    def load(self) -> None:
        self.PAGE.goto(self.URL)
