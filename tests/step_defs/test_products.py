# import pytest
from pytest_bdd import scenarios, given, when, then
from playwright.sync_api import BrowserContext
from tests.pages.medi_entry_stage import EntryStage

import time


# Scenarios
scenarios('../features/products.feature')


# Given Steps
@given('the products page')
def step_impl(context: BrowserContext):
    entry_page = EntryStage(context.pages[0])
    entry_page.create_new_invoice()
    # entry_page.load()
    time.sleep(6)