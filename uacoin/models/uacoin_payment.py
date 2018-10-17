# -*- coding: utf-8 -*-

from odoo import models, fields


class UacoinPayment(models.Model):
    _name = "uacoin.payment"

    payment_date = fields.Datetime(string='Payment date')
    account_id = fields.Many2one('uacoin.account', string='Account')
    journal_id = fields.Many2one('account.journal', string='Cash or bank journal')
    payment_sum = fields.Float(string='Payment sum')
    comment = fields.Char(string='Comment')
    user_id = fields.Many2one('res.users', string='Responsible', default=lambda s: s.env.user)
