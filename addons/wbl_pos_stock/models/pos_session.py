# -*- coding: utf-8 -*-
#
#################################################################################
# Author      : Weblytic Labs Pvt. Ltd. (<https://store.weblyticlabs.com/>)
# Copyright(c): 2023-Present Weblytic Labs Pvt. Ltd.
# All Rights Reserved.
#
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
##################################################################################

from odoo import models


class InheritPosSession(models.Model):
    _inherit = 'pos.session'

    def _process_pos_ui_product_product(self, products):
        quantity = 1
        config = self.config_id
        for product in products:
            product_info = self.env['product.product'].browse(product['id']).get_product_info_pos(product['lst_price'], quantity, config.id)
            product["product_info"] = product_info
        return super()._process_pos_ui_product_product(products)
