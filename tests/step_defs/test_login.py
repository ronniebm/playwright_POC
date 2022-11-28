from pytest_bdd import scenarios, given, when, then, parsers
from tests.pages import LoginPage, EnvironmentPage, EntryStage
from tests.environment import *

# Scenarios
scenarios('../features/login.feature')


# Given Steps
@given('the icyte login page is displayed')
def step(analyst_context):
    login_page = LoginPage(analyst_context)
    login_page.load()
    analyst_context.current_page = login_page


# When Steps
@when(parsers.parse('the user performs a log in'))
def step(analyst_context):
    login_page = analyst_context.current_page
    login_page.fill_login_credentials()
    env_page = EnvironmentPage(login_page.click_sign_in_btn())
    analyst_context.current_page = env_page


@when('the user set client and service area')
def step(analyst_context):
    env_page = analyst_context.current_page
    env_page.select_client_and_service()
    entry_page = EntryStage(env_page.click_submit_btn())
    analyst_context.current_page = entry_page


# Then Steps
@then('is redirected to the entry page')
def step(analyst_context):
    entry_page = analyst_context.current_page
