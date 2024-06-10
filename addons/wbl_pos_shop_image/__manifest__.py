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
	'name': 'Shop Image Uploader for POS',
	'version': '17.0.1.0.0',
	'summary': """The Odoo POS Shop Image Uploader is a feature-enhancing app designed for Odoo Point of Sale (POS) systems.
    It addresses the absence of shop images in the POS system by providing a user-friendly solution. With this app, 
    administrators can upload images for individual shops, enhancing the visual experience for users within the POS window.""",
	'description': """The Odoo POS Shop Image Uploader is a feature-enhancing app designed for Odoo Point of Sale (POS)
    systems. It addresses the absence of shop images in the POS system by providing a user-friendly solution. 
    With this app, administrators can upload images for individual shops, enhancing the visual experience 
    for users within the POS window.""",
	'category': 'Point of Sale',
	'author': 'Weblytic Labs',
	'company': 'Weblytic Labs',
	'website': "https://store.weblyticlabs.com",
	'depends': ['base', 'point_of_sale', 'mail', 'account', 'sale_management'],
	'data': [
		'views/point_of_sale_dashboard.xml',
		'views/pos_config_view.xml',
	],
	'assets': {
		'web.assets_backend': [
			'wbl_pos_shop_image/static/src/pos_shop_image/pos_shop_image.css',
		],
	},
	'images': ['static/description/banner.gif'],
	'license': 'OPL-1',
	'installable': True,
	'auto_install': False,
	'application': True,
}
