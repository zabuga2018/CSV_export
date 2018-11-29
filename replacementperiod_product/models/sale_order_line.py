# -*- coding: utf-8 -*-

from odoo import api, models, fields
from datetime import date


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    pricelist = fields.Many2one(related='product_id.pricelist_id', string='Pricelist', readonly=True)
    order_name = fields.Char(related='order_id.name', string='Order Number', readonly=True)
    order_confirmation_date = fields.Datetime(related='order_id.confirmation_date', string='Order Date', readonly=True)
    daystoreplacement = fields.Integer(string='Days left to replacement', compute='_compute_daystoreplacement')
    qty_available = fields.Float(related='product_id.qty_available', string='Quantity On Hand')
    is_email_sent = fields.Boolean(string='Email sent')
    is_call_made = fields.Boolean(string='Call made')
    
    @api.multi
    def _compute_daystoreplacement(self):
        for record in self:
            if not record.order_id.confirmation_date:
                record.daystoreplacement = date.today().timetuple().tm_yday -fields.Datetime.from_string(record.order_id.create_date).timetuple().tm_yday+record.product_id.replacement_period
            else:
                record.daystoreplacement = date.today().timetuple().tm_yday-fields.Datetime.from_string(record.order_id.confirmation_date).timetuple().tm_yday+record.product_id.replacement_period
