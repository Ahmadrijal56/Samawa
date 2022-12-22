from odoo import models, fields, api


class Marketing_fee(models.Model):
    _name = 'samawa_spektrum.marketing_fee'
    _description = 'samawa_spektrum.marketing_fee'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')