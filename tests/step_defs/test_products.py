# import pytest
from pytest_bdd import scenarios, given, when, then
from playwright.sync_api import BrowserContext, Browser
from tests.pages.products import ProductsPage

import time


# Scenarios
scenarios('../features/products.feature')


# Given Steps
@given('I go to the products page')
def step(analyst_context):
    products_page = ProductsPage(analyst_context)
    products_page.load()
    analyst_context.current_page = products_page


@when('I add a new product manually')
def step(analyst_context, api, tools):
    products_page = analyst_context.current_page
    products_page.click_add_new_product_btn()
    products_page.MODAL_ADD_PRODUCT_click_cancel_btn()
    time.sleep(5)
    # products_list = api.get_api_common_products(filter='ndc11')
    # new_product = tools.generate_new_product(products_list)
    # assert False, new_product
    pass
    # products_page.add_new_product()
    # approvals_page = ApprovalsPage(products_page.go_to_approvals())


# @given('the products page')
# def step_impl(login_context):
#     products_page = ProductsPage(login_context)
#     products_page.load()
