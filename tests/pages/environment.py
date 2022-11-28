from playwright.sync_api import BrowserContext
from tests.environment import *
from tests import Locators


class EnvironmentPage(Locators):

    def __init__(self, context: BrowserContext) -> None:
        super().__init__(context)
        self.PAGE = context.pages[0] if context.pages else context.new_page()
        self.URL = f'{ENV_URL}/environment'

    def load(self) -> None:
        self.PAGE.goto(self.URL)

    def close(self) -> None:
        self.PAGE.context.pages[0].close()

    def select_client_and_service(self) -> None:
        self.LOCATORS.environment_page.select_client()
        self.LOCATORS.environment_page.select_service()

    def click_submit_btn(self) -> BrowserContext:
        self.LOCATORS.environment_page.click_submit_btn()
        return self.PAGE.context
