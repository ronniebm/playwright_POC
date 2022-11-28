from playwright.sync_api import BrowserContext
from tests.environment import *
from tests import Locators, Api, Tools


class ProductsPage(Locators):

    def __init__(self, context: BrowserContext) -> None:
        super().__init__(context)
        self.PAGE = context.pages[0] if context.pages else context.new_page()
        self.URL = f'{ENV_URL}/masterdata/products'
        self.API = Api(context)
        self.TOOLS = Tools()

        # this attribute allow steps to use "modal_add_product" locators 'click' actions.
        self.modal_add_product = self.LOCATORS.products_page.modal_add_product

    def load(self) -> None:
        self.PAGE.goto(self.URL)

    def close(self) -> None:
        self.PAGE.context.pages[0].close()

    def click_add_new_product_btn(self) -> None:
        self.LOCATORS.products_page.click_add_new_product_btn()

    def fill_add_new_product_form(self) -> None:
        products_list = self.API.get_api_common_products(filter='ndc11')
        new_product = self.TOOLS.generate_new_product(products_list)

        # *NOTE: <Dict>.values() destructuring works for Python --version >= 3.6.
        manufacturer_name, ndc11, product_name, summary_name, brand_name,\
            market_date, sale_date, fda_approval_date, purchase_date, effective_date,\
            last_lot_date, cms_expiry_date, unit_c_factor, elegibility_start_date, \
            elegibility_end_date, medi_c_factor = new_product.values()

        # filling out "general_tab" form --------------
        self.LOCATORS.products_page.modal_add_product.fill_manufacturer_name(manufacturer_name)
        self.LOCATORS.products_page.modal_add_product.fill_ndc11(ndc11)
        self.LOCATORS.products_page.modal_add_product.fill_product_name(product_name)
        self.LOCATORS.products_page.modal_add_product.fill_summary_name(summary_name)
        self.LOCATORS.products_page.modal_add_product.fill_brand_name(brand_name)
        self.LOCATORS.products_page.modal_add_product.set_market_date(market_date)
        self.LOCATORS.products_page.modal_add_product.set_sale_date(sale_date)
        self.LOCATORS.products_page.modal_add_product.set_fda_approval_date(fda_approval_date)
        self.LOCATORS.products_page.modal_add_product.set_purchase_date(purchase_date)
        self.LOCATORS.products_page.modal_add_product.set_effective_date(effective_date)
        self.LOCATORS.products_page.modal_add_product.set_last_lot_date(last_lot_date)
        self.LOCATORS.products_page.modal_add_product.set_cms_expiry_date(cms_expiry_date)
        self.LOCATORS.products_page.modal_add_product.select_medical_elegibility()
        self.LOCATORS.products_page.modal_add_product.select_sale_uom()
        self.LOCATORS.products_page.modal_add_product.select_unit_uom()
        self.LOCATORS.products_page.modal_add_product.fill_unit_c_factor(unit_c_factor)
        self.LOCATORS.products_page.modal_add_product.select_drug_type()
        self.LOCATORS.products_page.modal_add_product.select_status()
        self.LOCATORS.products_page.modal_add_product.set_elegibility_start_date(elegibility_start_date)
        self.LOCATORS.products_page.modal_add_product.set_elegibility_end_date(elegibility_end_date)

        # filling out "govt_pricing_tab" form --------------
        self.LOCATORS.products_page.modal_add_product.click_govt_pricing_tab()
        self.LOCATORS.products_page.modal_add_product.select_asp_elegibility()
        self.LOCATORS.products_page.modal_add_product.select_nfamp_elegibility()
        self.LOCATORS.products_page.modal_add_product.select_amp_elegibility()
        self.LOCATORS.products_page.modal_add_product.select_bp_elegibility()
        self.LOCATORS.products_page.modal_add_product.select_iff_elegibility()
        self.LOCATORS.products_page.modal_add_product.select_asp_reportability()
        self.LOCATORS.products_page.modal_add_product.select_nfamp_reportability()
        self.LOCATORS.products_page.modal_add_product.select_amp_reportability()
        self.LOCATORS.products_page.modal_add_product.select_bp_reportability()
        self.LOCATORS.products_page.modal_add_product.select_iff_reportability()
        self.LOCATORS.products_page.modal_add_product.select_drug_category()
        self.LOCATORS.products_page.modal_add_product.select_desi_code()
        self.LOCATORS.products_page.modal_add_product.select_medi_cod_status()
        self.LOCATORS.products_page.modal_add_product.select_dosage()
        self.LOCATORS.products_page.modal_add_product.select_medicaid_uom()
        self.LOCATORS.products_page.modal_add_product.select_amp_type()
        self.LOCATORS.products_page.modal_add_product.select_i5_route()
        self.LOCATORS.products_page.modal_add_product.select_i5_threshold()
        self.LOCATORS.products_page.modal_add_product.fill_medi_c_factor(medi_c_factor)
        self.LOCATORS.products_page.modal_add_product.select_line_extension_flag()
        self.LOCATORS.products_page.modal_add_product.select_pediatric_drug_blood_clotting_f()
