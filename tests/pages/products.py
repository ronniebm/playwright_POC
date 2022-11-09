from playwright.sync_api import Page, BrowserContext
from tests.locators import Locators
from tests.environment import *


class ProductsPage(Locators):

    def __init__(self, context: BrowserContext) -> None:
        super().__init__(context)
        self.PAGE = context.new_page()
        self.CLOSE_PAGE = context.pages[0]
        self.URL = f'{ENV_URL}/masterdata/products'

    def load(self) -> None:
        self.PAGE.goto(self.URL)

    def close(self) -> None:
        self.CLOSE_PAGE.close()

    def click_add_new_product_btn(self):
        self.LOCATORS.products_page.click_add_new_product_btn()

    def MODAL_ADD_PRODUCT_click_cancel_btn(self):
        self.LOCATORS.products_page.modal_add_product.click_cancel_btn()
