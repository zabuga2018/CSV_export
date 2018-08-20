# -*- coding: utf-8 -*-
from odoo import api, fields, models
#from odoo import exceptions


class TypeOrder(models.Model):
    _name = "type.order"

    name = fields.Char(size=10)
   
#    @api.multi
#    def do_export(self):
#        raise exceptions.Warning('Выгрузка в процессе разработки!')
