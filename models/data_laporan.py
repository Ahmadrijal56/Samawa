from odoo import models, fields, api


class data_laporan(models.Model):
    _name = 'samawa_spektrum.data_laporan'
    _description = 'samawa_spektrum.data_laporan'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')