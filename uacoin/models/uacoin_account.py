# -*- coding: utf-8 -*-

import logging
from odoo import api, models, fields

_logger = logging.getLogger(__name__)


class UacoinAccount(models.Model):
    _name = "uacoin.account"
    _rec_name = 'partner_id'

    partner_id = fields.Many2one('res.partner', string='Customer')
    partner_phone = fields.Char(related='partner_id.phone', string='Customer phone', readonly=True)
    account_size = fields.Selection([(500, 500),(1000, 1000),(2000, 2000)],string='size of accaunt')
    payments_amount = fields.Float(string='amount of all payments', compute='_compute_amount_balance')
    balance = fields.Float(string='balance to be paid', compute='_compute_amount_balance')
    payment_ids = fields.One2many('uacoin.payment','account_id', 'Payments')

    @api.multi
    @api.depends('account_size', 'payment_ids')
    def _compute_amount_balance(self):
        for record in self:
            record.payments_amount = sum([payment.payment_sum for payment in record.payment_ids])
            record.balance = record.account_size - record.payments_amount
