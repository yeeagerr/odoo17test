# -*- coding: utf-8 -*-
# from odoo import http


# class ./odoo/costumAddons/employee(http.Controller):
#     @http.route('/./odoo/costum_addons/employee/./odoo/costum_addons/employee', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/./odoo/costum_addons/employee/./odoo/costum_addons/employee/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('./odoo/costum_addons/employee.listing', {
#             'root': '/./odoo/costum_addons/employee/./odoo/costum_addons/employee',
#             'objects': http.request.env['./odoo/costum_addons/employee../odoo/costum_addons/employee'].search([]),
#         })

#     @http.route('/./odoo/costum_addons/employee/./odoo/costum_addons/employee/objects/<model("./odoo/costum_addons/employee../odoo/costum_addons/employee"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('./odoo/costum_addons/employee.object', {
#             'object': obj
#         })

