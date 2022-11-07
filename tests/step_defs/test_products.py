# import pytest
from pytest_bdd import scenarios, given, when, then
from playwright.sync_api import BrowserContext, Browser
from tests.pages.products import ProductsPage

import time


# Scenarios
scenarios('../features/products.feature')


# Given Steps
@given('the products page')
def step_impl(context: BrowserContext, browser: Browser):
    new_context = browser.new_context(storage_state="state.json").new_page()
    # entry_page = EntryStage(context.pages[0])
    products_page = ProductsPage(new_context)
    products_page.load()
    # entry_page.load()
    time.sleep(3)
