# -*- coding: utf-8 -*-

from odoo import api, models, fields


class SaleOrder(models.Model):
    _inherit = "sale.order"

    barcode_sequence = fields.Char(string='Barcode for sale order', size=10)
    
    @api.model
    def create(self, vals):
        seq = self.env['ir.sequence'].next_by_code('barcode.sale.order') or '/'
        vals['barcode_sequence'] = seq
        return super(SaleOrder, self).create(vals)