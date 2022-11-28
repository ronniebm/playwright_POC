import random


class Tools:

    @staticmethod
    def generate_new_product(products_list: list) -> dict:
        assert isinstance(products_list, list), "*ERROR: 'products_list' value must be 'list' type !"
        new_ndc11 = str(random.randint(55000000000, 55999999999))

        while new_ndc11 in products_list:
            new_ndc11 = str(random.randint(55000000000, 55999999999))
        return {
                    'manufacturer_name': f'Automation Test Manufacturer',
                    'ndc11': new_ndc11,
                    'product_name': f'product_name_{new_ndc11}',
                    'summary_name': f'summary_name_{new_ndc11}',
                    'brand_name': f'brand_name_{new_ndc11}',
                    'market_date': '2007-01-15',
                    'sale_date': '2007-01-17',
                    'fda_approval_date': '2007-01-15',
                    'purchase_date': '2007-01-17',
                    'effective_date': '2030-01-17',
                    'last_lot_date': '2030-01-15',
                    'cms_expiry_date': '2031-01-15',
                    'unit_c_factor': '1',
                    'elegibility_start_date': '2007-01-15',
                    'elegibility_end_date': '2030-01-15',
                    'medi_c_factor': '1'
        }
