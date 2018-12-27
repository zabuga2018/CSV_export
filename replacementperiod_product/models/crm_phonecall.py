# -*- coding: utf-8 -*-

from odoo import api, models, fields


class CrmPhonecall(models.Model):
    _inherit = "crm.phonecall"
    
    order_id = fields.Many2one('sale.order', 'Sale Order')
    order_line_id = fields.Many2one('sale.order.line', 'Sale Order Line')

    @api.model
    def create(self, values):
       print("create phonecall")
       newrec = super(CrmPhonecall, self).create(values)
       if newrec.order_line_id:
            #newrec.order_line_id.is_call_made = True
            newrec.order_line_id.write({'is_call_made': True})
           
       return newrec
