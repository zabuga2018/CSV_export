# -*- coding: utf-8 -*-
import base64
import csv

from odoo import api, fields, models
from odoo import exceptions


class export_to_csv(models.TransientModel):
    _name = 'export_to_csv.wizard'

    filename = fields.Char(help="file name to export?")
    user_id = fields.Many2one('res.users',
                              string='Responsible',
                              default=lambda s: s.env.user)
    product_ids = fields.Many2many('product.product', string='Products')
    partner_id = fields.Many2one('res.partner', string='Partner')
   
    @api.multi
    def do_export(self):
        #chek filename
        if self.filename =='':
            raise exceptions.Warning('Не указано название файла! Выгрузка не выполнена')
        
        list_stockquant_csv = [["код товара", "наименование товара", "артрикул товара", "цена товара"]]
        list_stocklocation_ids = []
        
        #stock.quant to list
        current_product_id = 0
        stock_quants = self.env['stock.quant'].search([('product_id', 'in', self.product_ids.ids), ('location_id.usage', 'like', 'internal')],order = 'product_id')
        for stock_quant in stock_quants:
            if current_product_id != stock_quant.product_id.id:
                list_stockquant_csv.append([stock_quant.product_id.id, stock_quant.product_id.name, stock_quant.product_id.default_code, stock_quant.product_id.list_price])
                current_product_id = stock_quant.product_id.id
                for i in range(list_stocklocation_ids.__len__()):
                    list_stockquant_csv[list_stockquant_csv.__len__()-1].append(0)
            if list_stocklocation_ids.count(stock_quant.location_id.id) == 0:
                    list_stocklocation_ids.append(stock_quant.location_id.id)
                    list_stockquant_csv[0].append("склад "+stock_quant.location_id.name)
                    list_stockquant_csv[list_stockquant_csv.__len__()-1].append(stock_quant.quantity)
            else:            
                list_stockquant_csv[list_stockquant_csv.__len__()-1][4+list_stocklocation_ids.index(stock_quant.location_id.id)] = stock_quant.quantity 
            
        #list to file
        fp = open(self.filename, 'w')
        csvfile = csv.writer(fp)
        csvfile.writerows(list_stockquant_csv)
        fp.close()
            
        return True
    
    @api.multi
    def do_send_csv(self):
        self.do_export()
        template = self.env.ref('export_to_csv.export_to_csv_email_template')
        
        fp = open(self.filename, 'r')
        bynaryfile = base64.b64encode(fp.read().encode(encoding='utf-8'))
        fp.close()
        attachment_data = {
               'name': str(self.filename),
               'datas': bynaryfile,
               'datas_fname': self.filename,
               'res_model': 'mail.message',
           }
        attachment_id = self.env['ir.attachment'].create(attachment_data)
        
        self.env['mail.template'].browse(template.id).send_mail(self.id,email_values={'attachment_ids':[attachment_id.id]})
        return True
        
    