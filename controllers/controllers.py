# -*- coding: utf-8 -*-
# from odoo import http


# class CustomAddons/hotel(http.Controller):
#     @http.route('/custom_addons/hotel/custom_addons/hotel', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_addons/hotel/custom_addons/hotel/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_addons/hotel.listing', {
#             'root': '/custom_addons/hotel/custom_addons/hotel',
#             'objects': http.request.env['custom_addons/hotel.custom_addons/hotel'].search([]),
#         })

#     @http.route('/custom_addons/hotel/custom_addons/hotel/objects/<model("custom_addons/hotel.custom_addons/hotel"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_addons/hotel.object', {
#             'object': obj
#         })

