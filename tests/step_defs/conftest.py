#
# import pytest
# from pytest_bdd import scenarios, given, when, then
# from playwright.sync_api import Page, BrowserContext
# from tests.environment_vars import *
#
# from tests.pages.login import LoginPage
# from tests.pages.environment import EnvironmentPage
#

# @pytest.fixture
# def login(page: Page, context: BrowserContext) -> None:
#     login_page = LoginPage(page)
#     login_page.load()
#     env_page = EnvironmentPage(login_page.login(*ANALYST_CREDENTIALS))
#     env_page.set_client_and_service(*CLIENT_AND_SERVICE)
#     context.storage_state(path="state.json")

# Scenarios
# scenarios('../features/regression.feature')
#
#
# @given('the icyte login page is displayed')
# def step_impl(context: BrowserContext):
#     login_page = LoginPage(context.new_page())
#     login_page.load()
#     context.current_page = login_page
