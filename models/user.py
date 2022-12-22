from odoo import models, fields, api


class User(models.Model):
    _name = 'samawa_spektrum.user'
    _description = 'samawa_spektrum.user'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')