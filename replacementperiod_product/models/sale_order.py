# -*- coding: utf-8 -*-

from odoo import api, models, fields


class SaleOrder(models.Model):
    _inherit = "sale.order"

    phonecall_count = fields.Integer(
        compute='_compute_phonecall_count',
        string="Phonecalls",
    )
    
    @api.model
    def _compute_phonecall_count(self):
        for order in self:
            order.phonecall_count = self.env[
                'crm.phonecall'].search_count(
                [('order_id', '=', order.id)])
