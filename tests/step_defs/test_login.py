import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from playwright.sync_api import BrowserContext
from tests.pages.login import LoginPage
from tests.pages.environment import EnvironmentPage
from tests.pages.medi_entry_stage import EntryStage

from tests.environment_vars import *
import time


# Scenarios
scenarios('../features/login.feature')


# Given Steps
@given('the icyte login page is displayed')
def step_impl(context: BrowserContext):
    login_page = LoginPage(context.new_page())
    login_page.load()
    context.current_page = login_page


# When Steps
@when(parsers.parse('the user performs a log in'))
def step_impl(context: BrowserContext):
    login_page = context.current_page
    env_page = EnvironmentPage(login_page.login(*ANALYST_CREDENTIALS))
    context.current_page = env_page

@when('the user set client and service area')
def step_impl(context: BrowserContext):
    env_page = context.current_page
    entry_page = EntryStage(env_page.set_client_and_service(*CLIENT_AND_SERVICE))
    context.current_page = entry_page


# Then Steps
@then('is redirected to the entry page')
def step_impl(context: BrowserContext):
    entry_page = context.current_page
    context.storage_state(path="state.json")
    time.sleep(10)
