from odoo import models, fields, api


class Dashboard(models.Model):
    _name = 'samawa_spektrum.dashboard'
    _description = 'samawa_spektrum.dashboard'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')