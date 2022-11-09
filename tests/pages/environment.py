from playwright.sync_api import Page
from tests.environment import *


class EnvironmentPage:

    URL = f'{ENV_URL}/environment'

    def __init__(self, page: Page) -> None:
        self.PAGE = page
        self.CLIENT_DD = page.locator('#client-selector')
        self.SERVICE_AREA_DD = page.locator('#service-selector')
        self.SUBMIT_BUTTON = page.locator('text=Submit')

    def load(self) -> None:
        self.PAGE.goto(self.URL)

    def set_client_and_service(self, client: str, service_area: str) -> Page:
        self.CLIENT_DD.select_option(label=client)
        self.SERVICE_AREA_DD.select_option(label=service_area)
        self.SUBMIT_BUTTON.click()
        return self.PAGE
