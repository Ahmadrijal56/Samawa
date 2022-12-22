from odoo import models, fields, api


class Transaksi(models.Model):
    _name = 'samawa_spektrum.transaksi'
    _description = 'samawa_spektrum.transaksi'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')