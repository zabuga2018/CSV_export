# -*- coding: utf-8 -*-

from odoo.tests.common import TransactionCase
from datetime import date


class TestUacoin(TransactionCase):

    def setUp(self):
        super(TestUacoin, self).setUp()
        self.user_id = self.env.ref('base.user_root').id
        self.env = self.env(user=self.user_id)
        self.uacoin_account_model = self.env['uacoin.account']
        self.uacoin_payment_model = self.env['uacoin.payment']
        self.partner_test = self.env['res.partner'].create({'name': 'test_partner'})
        self.bank_journal_euro = self.env['account.journal'].create({'name': 'Bank', 'type': 'bank', 'code': 'BNK67'})

    def test_create_acoount(self, account_size = 2000):
        account = self.uacoin_account_model.create({
            'partner_id': self.partner_test.id,
            'account_size': account_size,
            })
        return account
    
    def test_create_payment(self, account_id=None, payment_sum = 520):
        payment = self.uacoin_payment_model.create({
            'payment_date': date.today(),
            'account_id': account_id,
            'journal_id': self.bank_journal_euro.id,
            'payment_sum': payment_sum,
            'comment': 'comment1',
            'user_id': self.user_id,
            })
    
    def test_compute_amount_balance(self):
        account = self.test_create_acoount()
        self.test_create_payment(account_id=account.id)
        self.assertEqual(account.payments_amount, 520)
        self.assertEqual(account.balance, 1480)
