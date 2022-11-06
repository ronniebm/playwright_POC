from playwright.sync_api import BrowserContext
from tests.api.common import Common


class Api(Common):
    def __init__(self, context: BrowserContext) -> None:
        super().__init__(context)
