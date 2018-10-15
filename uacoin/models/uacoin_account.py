# -*- coding: utf-8 -*-

from odoo import api, models, fields


class UacoinAccount(models.Model):
    _name = "uacoin.account"
    _rec_name = 'partner_id'
    
    @api.one
    @api.depends('account_size', 'payment_ids')
    def _compute_amount_balance(self):
        self.payments_amount = sum([payment.payment_sum for payment in self.payment_ids])
        self.balance = self.account_size - self.payments_amount
        
        
    partner_id = fields.Many2one('res.partner', string='Customer')
    partner_phone = fields.Char(related='partner_id.phone', string='Customer phone')
    account_size = fields.Selection([(500, 500),(1000, 1000),(2000, 2000)],string='size of accaunt')
    payments_amount = fields.Float(string='amount of all payments', compute='_compute_amount_balance')
    balance = fields.Float(string='balance to be paid', compute='_compute_amount_balance')
    payment_ids = fields.One2many('uacoin.payment','account_id', 'Payments')
