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

    def test_create(self):
        account = self.uacoin_account_model.create({
            'partner_id': self.partner_test.id,
            'account_size': 2000,
            })
        payment = self.uacoin_payment_model.create({
            'payment_date': date.today(),
            'account_id': account.id,
            'journal_id': self.bank_journal_euro.id,
            'payment_sum': 520,
            'comment': 'comment1',
            'user_id': self.user_id,
            })
        # self.uacoin_account_model._compute_amount_balance()
        self.assertEqual(account.payments_amount, 520)
        self.assertEqual(account.balance, 1480)
        '''
        print('size of account '+account.account_size.__str__())
        print('payments amount '+account.payments_amount.__str__())
        print('balance '+account.balance.__str__())
        '''
