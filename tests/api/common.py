from playwright.sync_api import BrowserContext
from tests.api.api_config import ApiConfig
from tests.environment_vars import *


class Common(ApiConfig):

    def __init__(self, context: BrowserContext) -> None:
        super().__init__(context)

    def get_api_common_clients(self):
        return self.api.get(f'{ENV_URL}/api/common/clients/').json()
