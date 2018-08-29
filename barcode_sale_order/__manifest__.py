# -*- coding: utf-8 -*-
{
    'name': 'Sales orders barcodes',
    'description': 'Adds barcodes to sale orders',
    'author': 'Alexey Zabuga',
    'depends': ['base', 'sale', 'type_order'],
    'data': [
            'data/barcode_sale_order_data.xml',
            'report/report_sale_order.xml',
            'views/inherited_sale_order_view.xml',
            ],
}
