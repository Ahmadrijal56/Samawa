from odoo import models, fields, api


class data_laporan_batal(models.Model):
    _name = 'samawa_spektrum.data_laporan_batal'
    _description = 'samawa_spektrum.data_laporan_batal'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')