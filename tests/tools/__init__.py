import random


class Tools:

    @staticmethod
    def generate_new_product(products_list: list) -> int:
        assert isinstance(products_list, list), "*ERROR: 'products_list' value must be 'list' type !"
        new_ndc11 = random.randint(55000000000, 55999999999)

        while new_ndc11 in products_list:
            new_ndc11 = random.randint(55000000000, 55999999999)
        return {

        }
