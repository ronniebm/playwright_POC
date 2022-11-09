from playwright.sync_api import BrowserContext
from tests.environment import *


class Common:
    def __init__(self, context: BrowserContext) -> None:
        self.API = context.request

    def get_api_common_clients(self) -> list:
        return self.API.get(f'{ENV_URL}/api/common/clients/').json()

    def get_api_common_products(self, filter: str = None) -> list:
        assert filter is None or filter is 'ndc11', "'filter:' parameter must be 'ndc11' (lower case)."
        products = self.API.get(f'{ENV_URL}/api/common/products/').json()
        if filter is "ndc11":
            new_array = []
            for product in products:
                new_array.append(product["ndc11"])
            return new_array
        return products
