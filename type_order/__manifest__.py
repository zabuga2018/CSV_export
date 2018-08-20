# -*- coding: utf-8 -*-
{
    'name': 'Sales orders types',
    'description': 'Adds types for sale orders',
    'author': 'Alexey Zabuga',
    'depends': ['base', 'sale'],
    'data': [
            'security/ir.model.access.csv',
            'views/inherited_sale_order_view.xml',
            'views/type_order_view.xml',
            ],
}
