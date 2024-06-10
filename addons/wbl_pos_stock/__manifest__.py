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

{
    'name': 'POS Stock Quantity Pro',
    'version': '17.0.1.0.0',
    'summary': """Save time by showing useful information about products on the POS window.""",
    'description': """Save time by showing useful information about products on the POS window.""",
    'category': 'Point of Sale',
    'author': 'Weblytic Labs',
    'company': 'Weblytic Labs',
    'website': "https://store.weblyticlabs.com",
    'depends': ['base', 'mail', 'point_of_sale', 'stock', 'account', 'sale_management'],
    'data': [
        'views/res_config_settings_views.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'wbl_pos_stock/static/src/xml/product_card.xml',
            'wbl_pos_stock/static/src/xml/product_list.xml',
            'wbl_pos_stock/static/src/js/product_card.js',
            'wbl_pos_stock/static/src/js/product_list.js',
            'wbl_pos_stock/static/src/js/models.js',
        ],
    },
    'images': ['static/description/banner.gif'],
    'license': 'OPL-1',
    'installable': True,
    'auto_install': False,
    'application': True,
}
