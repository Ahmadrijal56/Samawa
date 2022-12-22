from odoo import models, fields, api


class samawa(models.Model):
    _name = 'samawa.samawa'
    _description = 'samawa.samawa'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
