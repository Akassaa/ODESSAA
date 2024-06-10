 
{
    'name': 'POS restaurant depend',
    'category': 'Website',
    'version': "17.0.1.0.1",
    'author': 'Terabits Technolab ',
    'website': 'https://www.terabits.xyz/apps/17.0/pos_restaurant_depends_bits',
    'summary': 'This module contains pos restaurant-related customizations depending on delight_pos_theme_bits',
    'description': """ This module contains pos restaurant-related customizations depending on delight_pos_theme_bits """,
    'depends': [
        'pos_restaurant',   
    ],
    'assets': {
        "point_of_sale._assets_pos": [ 
            '/pos_restaurant_depends_bits/static/src/js/popup_ord_items.js',
            '/pos_restaurant_depends_bits/static/src/xml/popup_ord_items.xml',
            '/pos_restaurant_depends_bits/static/src/scss/popup.scss',
            '/pos_restaurant_depends_bits/static/src/js/FloorScreen.js',
            '/pos_restaurant_depends_bits/static/src/xml/actionpad_widget.xml',
            '/pos_restaurant_depends_bits/static/src/js/ActionpadWidget.js',
            '/pos_restaurant_depends_bits/static/src/xml/category_selector.xml' 
        ],
    },
    'images': [
        'static/description/banner.png'
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'OPL-1', 
}
