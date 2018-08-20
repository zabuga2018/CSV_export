# -*- coding: utf-8 -*-
from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = "sale.order"

    typeorder = fields.Many2one('type.order', string='Type order')
