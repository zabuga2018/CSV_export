# -*- coding: utf-8 -*-
from odoo import api, fields, models


class TypeOrder(models.Model):
    _name = "sale.order.type"

    name = fields.Char('Name of type', size=10)
