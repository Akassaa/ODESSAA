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

from odoo import fields, models


class InheritPosConfig(models.Model):
    _inherit = 'pos.config'

    is_display_on_hand_qty = fields.Boolean(string="Display On Hand Qty in POS")
    is_display_forecasted_qty = fields.Boolean(string="Display Forecasted Qty in POS")
    is_display_tax = fields.Boolean(string="Display Tax in POS")
    restrict_zero_price_line = fields.Boolean(string="Restrict Zero Price Order Line")
    restrict_zero_qty_line = fields.Boolean(string="Restrict Zero Quantity Order Line")
    allow_order_for_out_of_stock = fields.Boolean(string="Allow POS Order When Product is Out of Stock")
    hide_out_of_stock_product = fields.Boolean(string="Hide Out Of Stock Products")
    deny_pos_order = fields.Char(string="Deny PoS Order")
    on_hand_bg_color = fields.Char(string="On Hand Background Color")
    on_hand_text_color = fields.Char(string="On Hand Text Color")
    forecasted_bg_color = fields.Char(string="Forecasted Background Color")
    forecasted_text_color = fields.Char(string="Forecasted Text Color")
    out_of_stock_bg_color = fields.Char(string="Out Of Stock Background Color")
    out_of_stock_text_color = fields.Char(string="Out Of Stock Text Color")
    custom_error_message = fields.Text(string="Custom Error Message")
