from odoo import models, fields, api


class data_laporan_penjualan(models.Model):
    _name = 'samawa_spektrum.data_laporan_penjualan'
    _description = 'samawa_spektrum.data_laporan_penjualan'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')