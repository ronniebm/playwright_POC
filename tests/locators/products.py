from playwright.sync_api import BrowserContext


# ---------------------------------------
# Locators for PAGE: Products.
# ---------------------------------------
class ProductLocators:

    def __init__(self, context: BrowserContext) -> None:
        self.PAGE = context
        self.modal_add_product = AddProductModalLocators(context)

    def click_add_new_product_btn(self):
        self.PAGE.pages[0].locator('i[class*=fa-plus]').click()


# ---------------------------------------
# Locators for MODAL WINDOW: Add Product.
# ---------------------------------------
class AddProductModalLocators:

    def __init__(self, context: BrowserContext) -> None:
        self.PAGE = context

    def click_cancel_btn(self):
        self.PAGE.pages[0].locator('#product-cancel-btn').click()
