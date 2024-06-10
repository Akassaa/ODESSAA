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


class InheritPosResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    is_display_on_hand_qty = fields.Boolean(
        related="pos_config_id.is_display_on_hand_qty",
        string="Display On Hand Qty in POS",
        readonly=False
    )
    is_display_forecasted_qty = fields.Boolean(
        related="pos_config_id.is_display_forecasted_qty",
        string="Display Forecasted Qty in POS",
        readonly=False
    )
    is_display_tax = fields.Boolean(
        related="pos_config_id.is_display_tax",
        string="Display Tax in POS",
        readonly=False
    )
    restrict_zero_price_line = fields.Boolean(
        related="pos_config_id.restrict_zero_price_line",
        string="Restrict Zero Price Order Line",
        readonly=False
    )
    restrict_zero_qty_line = fields.Boolean(
        related="pos_config_id.restrict_zero_qty_line",
        string="Restrict Zero Quantity Order Line",
        readonly=False
    )
    allow_order_for_out_of_stock = fields.Boolean(
        related="pos_config_id.allow_order_for_out_of_stock",
        string="Allow POS Order When Product is Out of Stock",
        readonly=False
    )
    hide_out_of_stock_product = fields.Boolean(
        related="pos_config_id.hide_out_of_stock_product",
        string="Hide Out Of Stock Products",
        readonly=False
    )
    deny_pos_order = fields.Char(
        related="pos_config_id.deny_pos_order",
        string="Deny PoS Order",
        readonly=False
    )
    on_hand_bg_color = fields.Char(
        related="pos_config_id.on_hand_bg_color",
        string="On Hand Background Color",
        readonly=False
    )
    on_hand_text_color = fields.Char(
        related="pos_config_id.on_hand_text_color",
        string="On Hand Text Color",
        readonly=False
    )
    forecasted_bg_color = fields.Char(
        related="pos_config_id.forecasted_bg_color",
        string="Forecasted Background Color",
        readonly=False
    )
    forecasted_text_color = fields.Char(
        related="pos_config_id.forecasted_text_color",
        string="Forecasted Text Color",
        readonly=False
    )
    out_of_stock_bg_color = fields.Char(
        related="pos_config_id.out_of_stock_bg_color",
        string="Out Of Stock Background Color",
        readonly=False
    )
    out_of_stock_text_color = fields.Char(
        related="pos_config_id.out_of_stock_text_color",
        string="Out Of Stock Text Color",
        readonly=False
    )
    custom_error_message = fields.Text(
        related="pos_config_id.custom_error_message",
        string="Custom Error Message",
        readonly=False
    )
