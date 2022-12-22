from odoo import models, fields, api


class Marketing(models.Model):
    _name = 'samawa_spektrum.marketing'
    _description = 'samawa_spektrum.marketing'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')