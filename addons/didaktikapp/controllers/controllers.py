# -*- coding: utf-8 -*-
# from odoo import http


# class Didaktikapp(http.Controller):
#     @http.route('/didaktikapp/didaktikapp', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/didaktikapp/didaktikapp/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('didaktikapp.listing', {
#             'root': '/didaktikapp/didaktikapp',
#             'objects': http.request.env['didaktikapp.didaktikapp'].search([]),
#         })

#     @http.route('/didaktikapp/didaktikapp/objects/<model("didaktikapp.didaktikapp"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('didaktikapp.object', {
#             'object': obj
#         })

