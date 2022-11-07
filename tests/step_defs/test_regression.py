import pytest
from pytest_bdd import scenarios, given, when, then
from playwright.sync_api import BrowserContext
from tests.pages.medi_entry_stage import EntryStage
import time


# Scenarios
# scenarios('../features/regression.feature')


# Given Steps
@given('a regression test')
def step_impl(context: BrowserContext):
    pass