# import pytest
from pytest_bdd import scenarios, given, when, then
from playwright.sync_api import BrowserContext
from tests.pages.login import LoginPage
from tests.pages.environment import EnvironmentPage
from tests.pages.medi_invoices_entry import EntryPage

from tests.environment_vars import *
import time

# Constants
# DUCKDUCKGO_HOME = 'https://duckduckgo.com/'

# Scenarios
scenarios('../features/login.feature')


# Fixtures
# @pytest.fixture
# def browser():
#     b = webdriver.Firefox()
#     b.implicitly_wait(10)
#     yield b
#     b.quit()

# Given Steps
@given('the icyte login page is displayed')
def step_impl(context: BrowserContext):
    login_page = LoginPage(context.new_page())
    login_page.load()
    context.current_page = login_page


# When Steps
@when('the user performs a log in')
def step_impl(context: BrowserContext):
    login_page = context.current_page
    env_page = EnvironmentPage(login_page.login(*ANALYST_CREDENTIALS))
    context.current_page = env_page


# Then Steps
@when('the user set client and service area')
def step_impl(context: BrowserContext):
    env_page = context.current_page
    entry_page = EntryPage(env_page.set_client_and_service(*CLIENT_AND_SERVICE))
    context.current_page = entry_page


@then('is redirected to the entry page')
def step_impl(context: BrowserContext):
    entry_page = context.current_page
    entry_page.create_new_invoice()
    time.sleep(6)
