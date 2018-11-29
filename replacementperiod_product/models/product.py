# -*- coding: utf-8 -*-

from odoo import api, models, fields


class ProductProduct(models.Model):
    _inherit = "product.product"

    replacement_period = fields.Integer(string='Replacement period', help='Replacement period unit of measure - days')
    url = fields.Char(string='URL', help='URL - http link')
    