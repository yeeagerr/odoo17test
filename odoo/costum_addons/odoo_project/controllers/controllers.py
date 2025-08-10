# -*- coding: utf-8 -*-
from odoo import http


class OdooProject(http.Controller):
    @http.route('/odoo_project/odoo_project', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/odoo_project/odoo_project/objects', auth='public')
    def list(self, **kw):
        return http.request.render('odoo_project.listing', {
            'root': '/odoo_project/odoo_project',
            'objects': http.request.env['odoo.project'].search([]),
        })

    @http.route('/odoo_project/odoo_project/objects/<model("odoo_project.odoo_project"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('odoo_project.object', {
            'object': obj
        })

