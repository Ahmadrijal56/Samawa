from odoo import models, fields, api


class data_laporan_resumeharian(models.Model):
    _name = 'samawa_spektrum.data_laporan_resumeharian'
    _description = 'samawa_spektrum.data_laporan_resumeharian'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')