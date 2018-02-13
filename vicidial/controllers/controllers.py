# -*- coding: utf-8 -*-
from odoo import http

# class Vicidial(http.Controller):
#     @http.route('/vicidial/vicidial/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vicidial/vicidial/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vicidial.listing', {
#             'root': '/vicidial/vicidial',
#             'objects': http.request.env['vicidial.vicidial'].search([]),
#         })

#     @http.route('/vicidial/vicidial/objects/<model("vicidial.vicidial"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vicidial.object', {
#             'object': obj
#         })