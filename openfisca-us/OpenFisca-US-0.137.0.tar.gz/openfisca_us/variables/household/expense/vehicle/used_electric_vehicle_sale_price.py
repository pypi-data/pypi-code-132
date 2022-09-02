from openfisca_us.model_api import *


class used_electric_vehicle_sale_price(Variable):
    value_type = float
    entity = TaxUnit
    unit = USD
    label = "Sale price of newly purchased used electric vehicle"
    definition_period = YEAR
    quantity_type = STOCK
