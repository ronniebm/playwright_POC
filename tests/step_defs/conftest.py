import pytest

from playwright.sync_api import Browser
from tests.environment import *
from tests.api import Api
from tests.tools import Tools

USER_AUTH_URL: str = f'{ENV_URL}/api/auth/login/'
ENV_AUTH_URL: str = f'{ENV_URL}/api/auth/environment/'
HEADERS: dict = {'Content-Type': 'application/json'}
ANALYST_DATA: dict = {"username": ANALYST_CREDENTIALS[0], "password": ANALYST_CREDENTIALS[1]}
MANAGER_DATA: dict = {"username": MANAGER_CREDENTIALS[0], "password": MANAGER_CREDENTIALS[1]}
CLIENT_AND_SERVICE_DATA: dict = {"client_id": 35, "service_id": 1}


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
def analyst_context(browser: Browser):
    """ Fixture: it builds an Analyst user context in background.
    --------------------------------------------------------------
    """
    context = browser.new_context(viewport=VIEWPORT)
    context.set_default_timeout(timeout=50000)
    context.request.post(USER_AUTH_URL, headers=HEADERS, data=ANALYST_DATA)
    context.request.post(ENV_AUTH_URL, headers=HEADERS, data=CLIENT_AND_SERVICE_DATA)
    # context.tracing.start(screenshots=True, snapshots=True)
    # context.tracing.stop(path='trace.zip')
    return context


@pytest.fixture(scope='module')
def manager_context(browser: Browser):
    """ Fixture: it builds a Manager user context in background.
    -------------------------------------------------------------
    """
    context = browser.new_context(viewport=VIEWPORT)
    context.set_default_timeout(timeout=50000)
    context.request.post(USER_AUTH_URL, headers=HEADERS, data=MANAGER_DATA)
    context.request.post(ENV_AUTH_URL, headers=HEADERS, data=CLIENT_AND_SERVICE_DATA)
    return context


@pytest.fixture(scope='module')
def api(analyst_context):
    """ Fixture: it builds an API context in background.
    -----------------------------------------------------
    """
    return Api(analyst_context)


@pytest.fixture(scope='module')
def tools():
    """ Fixture: it builds a Tools context in background.
    -----------------------------------------------------
    """
    return Tools
