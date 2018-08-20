# -*- coding: utf-8 -*-

from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = "sale.order"

    sale_order_type_id = fields.Many2one('sale.order.type', string='Type order')
