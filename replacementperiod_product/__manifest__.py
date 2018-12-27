# -*- coding: utf-8 -*-
{
    'name': 'Replacement period',
    'description': 'Adds fields replacement period, URL to product',
    'author': 'Alexey Zabuga',
    'depends': ['base', 'sale', 'product', 'crm_phonecall', 'mail'],
    'data': [
            'views/sale_order_line_view.xml',
            'views/inherited_product_view.xml',
            'views/inherited_crm_phonecall_view.xml',
            'views/inherited_sale_order_view.xml',
            ],
}
