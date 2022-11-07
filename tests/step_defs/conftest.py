import pytest
from playwright.sync_api import Browser
# from pytest_bdd import scenarios, given, when, then
# from playwright.sync_api import Page, BrowserContext
# from tests.environment_vars import *
#
# from tests.pages.login import LoginPage
# from tests.pages.environment import EnvironmentPage


@pytest.fixture(scope='session')
def data_files_dir(tmpdir_factory):
    """ Fixture: it creates a temp directory to store files.
    --------------------------------------------------------
    When the last test in your session terminates (regardless if it failed or passed),
    the directory will be removed automatically because of the tmpdir_factory fixture.
    --------------------------------------------------------
    see URL > https://docs.pytest.org/en/7.1.x/how-to/tmp_path.html#the-tmpdir-and-tmpdir-factory-fixtures
    """
    datadir = tmpdir_factory.mktemp('data')
    return datadir


@pytest.fixture(scope='module')
def login_context(browser: Browser, data_files_dir):
    """ Fixture: loading the user login saved content into a new Browser context.
    -------------------------------------------------------------------------
    This fixture uses data_files_dir fixture to access the temp data_files_dir.
    """
    return browser.new_context(storage_state=f'{data_files_dir}/state.json')
