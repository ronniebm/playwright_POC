from pytest_bdd import scenarios, given, when, then
from tests.pages import ProductsPage
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
def step(analyst_context, manager_context):
    # analyst_context.tracing.start(screenshots=True, snapshots=True)
    products_page = analyst_context.current_page
    products_page.click_add_new_product_btn()
    products_page.fill_add_new_product_form()
    products_page.modal_add_product.click_submit_btn()
    # manager context example
    products_page_manager = ProductsPage(manager_context)
    products_page_manager.load()
    time.sleep(5)
    products_page_manager.close()
    time.sleep(5)
    # analyst_context.tracing.stop(path='trace-create-product-manually.zip')
    analyst_context.current_page = products_page


@then('I confirm the product was placed in "PENDING" status')
def step(analyst_context):
    products_page = analyst_context.current_page
    analyst_context.current_page = products_page
