from playwright.sync_api import BrowserContext


class ApiConfig:
    def __init__(self, context: BrowserContext) -> None:
        self.api = context.request
