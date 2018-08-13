# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo import exceptions


class export_to_csv(models.TransientModel):
    _name = 'export_to_csv.wizard'

    flname = fields.Char(help="file name to export?")
    user_id = fields.Many2one(
        'res.users',
        string='Responsible',
        default=lambda s: s.env.user)
    product_ids = fields.Many2many('product.product', string='Products')
   
    @api.multi
    def do_export(self):
        raise exceptions.Warning('Выгрузка в процессе разработки!')
