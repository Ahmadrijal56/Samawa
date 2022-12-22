# -*- coding: utf-8 -*-
# from odoo import http


# class Samawa(http.Controller):
#     @http.route('/samawa/samawa', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/samawa/samawa/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('samawa.listing', {
#             'root': '/samawa/samawa',
#             'objects': http.request.env['samawa.samawa'].search([]),
#         })

#     @http.route('/samawa/samawa/objects/<model("samawa.samawa"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('samawa.object', {
#             'object': obj
#         })
