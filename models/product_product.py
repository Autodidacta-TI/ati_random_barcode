# -*- coding: utf-8 -*-
import random
from odoo import api, fields, models, _

class ProductProduct(models.Model):
    _inherit = 'product.product'

    def random_barcode(slef):
        return random.randint(1111111111111, 9999999999999)

    def generat_random_barcode(self):
        barcode = random.randint(1111111111111, 9999999999999)
        existing_product = self.search([('barcode', '=', barcode)])
        while len(existing_product) > 0:
            barcode = self.random_barcode()
            existing_product = self.search([('barcode', '=', barcode)])
        
        #assign barcode
        self.barcode = barcode