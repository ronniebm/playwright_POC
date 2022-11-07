# import pytest
from pytest_bdd import scenarios, given, when, then
from playwright.sync_api import BrowserContext, Browser
from tests.pages.products import ProductsPage

import time


# Scenarios
scenarios('../features/products.feature')


# Given Steps
@given('the products page')
def step_impl(login_context):
    products_page = ProductsPage(login_context)
    products_page.load()
