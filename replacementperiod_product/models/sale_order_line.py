# -*- coding: utf-8 -*-

from odoo import api, models, fields
from odoo import _
from datetime import date


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    pricelist = fields.Many2one(related='product_id.pricelist_id', string='Pricelist', readonly=True)
    order_name = fields.Char(related='order_id.name', string='Order Number', readonly=True)
    order_confirmation_date = fields.Datetime(related='order_id.confirmation_date', string='Order Date', readonly=True)
    days_to_replacement = fields.Integer(string='Days left to replacement', compute='_compute_days_to_replacement',  store = True)
    qty_available = fields.Float(related='product_id.qty_available', string='Quantity On Hand')
    is_email_sent = fields.Boolean(string='Email sent')
    is_call_made = fields.Boolean(string='Call made')
    
    @api.multi
    def _compute_days_to_replacement(self):
        for record in self:
            if record.product_id.replacement_period > 0: 
                if not record.order_id.confirmation_date:
                    record.days_to_replacement = date.today().timetuple().tm_yday -fields.Datetime.from_string(record.order_id.create_date).timetuple().tm_yday+record.product_id.replacement_period
                else:
                    record.days_to_replacement = date.today().timetuple().tm_yday-fields.Datetime.from_string(record.order_id.confirmation_date).timetuple().tm_yday+record.product_id.replacement_period
            else:
                record.days_to_replacement = 0
                
    @api.multi
    def action_email_sent(self):
        print('email sent')

    @api.multi        
    def action_call_made(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Make phonecall',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'crm.phonecall',
            'target': 'new',
            'context': {
                'default_name': _('Lens replacement phonecall'),
                'default_order_id': self.order_id.id,
                'default_order_line_id': self.id,
                'default_partner_id': self.order_partner_id.id,
                'default_partner_phone': self.order_partner_id.phone,
                'default_partner_mobile': self.order_partner_id.mobile,
                'default_state': 'done',
            }
        }
