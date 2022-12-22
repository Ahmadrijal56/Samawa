from odoo import models, fields, api


class data_laporan_jadwaltagihan(models.Model):
    _name = 'samawa_spektrum.data_laporan_jadwaltagihan'
    _description = 'samawa_spektrum.data_laporan_jadwaltagihan'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')