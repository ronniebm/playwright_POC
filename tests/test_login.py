from playwright.sync_api import Page, BrowserContext
from pages import LoginPage, EnvironmentPage, EntryPage


def test_user_login(page: Page, context: BrowserContext) -> None:
    login_page = LoginPage(page)
    environment_page = EnvironmentPage(page)
    entry_page = EntryPage(page)

    # Given the ICyte login page is displayed
    login_page.load()
    # When the user logged in.
    login_page.login('rbarrios', 'rbarrios123')

    # And the user set client and service area.
    environment_page.set_client_and_service_area('MannKind Corporation', 'Medicaid')

    # Then will be redirected to the entry stage.
    entry_page.create_new_invoice()

    request = context.request
    res = request.get('https://qa-icyte-sparc.integrichain.net/api/common/clients/')
    assert False, res.json()
