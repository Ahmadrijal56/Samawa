from odoo import models, fields, api


class Developer(models.Model):
    _name = 'samawa_spektrum.developer'
    _description = 'samawa_spektrum.developer'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')