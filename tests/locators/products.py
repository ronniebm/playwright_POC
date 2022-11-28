from playwright.sync_api import BrowserContext


# Locators for PAGE: Products.
# ---------------------------------------
class ProductLocators:

    def __init__(self, context: BrowserContext) -> None:
        self.PAGE = context
        self.modal_add_product = ModalAddProductLocators(context)

    def click_add_new_product_btn(self):
        self.PAGE.pages[0].locator('i[class*=fa-plus]').click()


# Locators for MODAL WINDOW: Add Product.
# ---------------------------------------
class ModalAddProductLocators:

    def __init__(self, context: BrowserContext) -> None:
        self.PAGE = context

    # ------------------------------
    # Click actions.
    def click_general_tab(self):
        self.PAGE.pages[0].locator('text=General').click(position={'x': -110, 'y': -43})

    def click_govt_pricing_tab(self):
        self.PAGE.pages[0].locator('text=Govt.').click(position={'x': -110, 'y': -43})

    def click_submit_btn(self):
        self.PAGE.pages[0].locator('#product-submit-btn').click()

    def click_cancel_btn(self):
        self.PAGE.pages[0].locator('#product-cancel-btn').click()

    # ------------------------------
    # [fill, set, select] actions for ModalAddProduct > General tab.
    def fill_manufacturer_name(self, value: str):
        self.PAGE.pages[0].locator('#manufacturer_name').fill(value)

    def fill_ndc11(self, value: str):
        self.PAGE.pages[0].locator('#ndc11').fill(value)

    def fill_product_name(self, value: str):
        self.PAGE.pages[0].locator('#product_name').fill(value)

    def fill_summary_name(self, value: str):
        self.PAGE.pages[0].locator('#product_summary_name').fill(value)

    def fill_brand_name(self, value: str):
        self.PAGE.pages[0].locator('#product_brand').fill(value)

    def set_market_date(self, value: str):
        self.PAGE.pages[0].locator('#market_date').fill(value)

    def set_sale_date(self, value: str):
        self.PAGE.pages[0].locator('#first_sale_date').fill(value)

    def set_fda_approval_date(self, value: str):
        self.PAGE.pages[0].locator('#fda_approval_date').fill(value)

    def set_purchase_date(self, value: str):
        self.PAGE.pages[0].locator('#purchase_date').fill(value)

    def set_effective_date(self, value: str):
        self.PAGE.pages[0].locator('#effective_date').fill(value)

    def set_last_lot_date(self, value: str):
        self.PAGE.pages[0].locator('#termination_date').fill(value)

    def set_cms_expiry_date(self, value: str):
        self.PAGE.pages[0].locator('#expiration_date').fill(value)

    def select_medical_elegibility(self, value: str = "Eligible"):
        self.PAGE.pages[0].locator('#flag_medi').select_option(label=value)

    def select_sale_uom(self, value: str = "Each"):
        self.PAGE.pages[0].locator('#sale_uom').select_option(label=value)

    def select_unit_uom(self, value: str = "Units"):
        self.PAGE.pages[0].locator('#unit_uom').select_option(label=value)

    def fill_unit_c_factor(self, value: str):
        self.PAGE.pages[0].locator('#unit_conversion_factor').fill(value)

    def select_drug_type(self, value: str = "Rx"):
        self.PAGE.pages[0].locator('#drug_type').select_option(label=value)

    def select_status(self, value: str = "Active"):
        self.PAGE.pages[0].locator('#flag_active').select_option(label=value)

    def set_elegibility_start_date(self, value: str):
        self.PAGE.pages[0].locator('#elig_start_date').fill(value)

    def set_elegibility_end_date(self, value: str):
        self.PAGE.pages[0].locator('#elig_end_date').fill(value)

    # ------------------------------
    # [fill, set, select] actions for ModalAddProduct > Govt_pricing tab.
    def select_asp_elegibility(self, value: str = "Eligible"):
        self.PAGE.pages[0].locator('#flag_asp').select_option(label=value)

    def select_nfamp_elegibility(self, value: str = "Eligible"):
        self.PAGE.pages[0].locator('#flag_nfamp').select_option(label=value)

    def select_amp_elegibility(self, value: str = "Eligible"):
        self.PAGE.pages[0].locator('#flag_amp').select_option(label=value)

    def select_bp_elegibility(self, value: str = "Eligible"):
        self.PAGE.pages[0].locator('#flag_bp').select_option(label=value)

    def select_iff_elegibility(self, value: str = "Eligible"):
        self.PAGE.pages[0].locator('#flag_iff').select_option(label=value)

    def select_asp_reportability(self, value: str = "Reportable"):
        self.PAGE.pages[0].locator('#reportable_asp').select_option(label=value)

    def select_nfamp_reportability(self, value: str = "Reportable"):
        self.PAGE.pages[0].locator('#reportable_nfamp').select_option(label=value)

    def select_amp_reportability(self, value: str = "Reportable"):
        self.PAGE.pages[0].locator('#reportable_amp').select_option(label=value)

    def select_bp_reportability(self, value: str = "Reportable"):
        self.PAGE.pages[0].locator('#reportable_bp').select_option(label=value)

    def select_iff_reportability(self, value: str = "Reportable"):
        self.PAGE.pages[0].locator('#reportable_iff').select_option(label=value)

    def select_drug_category(self, value: str = "Single Source"):
        self.PAGE.pages[0].locator('#drug_category').select_option(label=value)

    def select_desi_code(self, value: str = "02"):
        self.PAGE.pages[0].locator('#desi_code').select_option(label=value)

    def select_medi_cod_status(self, value: str = "01 - Abbreviated New Drug Application (ANDA)"):
        self.PAGE.pages[0].locator('#medi_cod_status').select_option(label=value)

    def select_dosage(self, value: str = "Capsule"):
        self.PAGE.pages[0].locator('#dosage_form').select_option(label=value)

    def select_medicaid_uom(self, value: str = "Capsules"):
        self.PAGE.pages[0].locator('#medicaid_uom').select_option(label=value)

    def select_amp_type(self, value: str = "5i"):
        self.PAGE.pages[0].locator('#amp_type').select_option(label=value)

    def select_i5_route(self, value: str = "000 - Not Applicable"):
        self.PAGE.pages[0].locator('#route_5i').select_option(label=value)

    def select_i5_threshold(self, value: str = "X - Not a 5i Drug"):
        self.PAGE.pages[0].locator('#threshold_5i').select_option(label=value)

    def fill_medi_c_factor(self, value: str):
        self.PAGE.pages[0].locator('#medicaid_conversion_factor').fill(value)

    def select_line_extension_flag(self, value: str = "True"):
        self.PAGE.pages[0].locator('#flag_line_extension').select_option(label=value)

    def select_pediatric_drug_blood_clotting_f(self, value: str = "PED"):
        self.PAGE.pages[0].locator('#ped_clot_factor').select_option(label=value)
