# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)

class EmployeeDirectory(models.Model):
    _name = 'employee.directory'    
    _description = "Employee Directory"

    name = fields.Char(string="Nama Karyawan")
    job_positon = fields.Char(string="Jabatan")
    depatement_id = fields.Many2one(comodel_name="hr.department", string="Departement")
    employee_id = fields.Many2one(comodel_name="hr.employee", string="Employee")
    phone = fields.Char(string="Nomor Telepon")
    image = fields.Binary()

    @api.onchange('employee_id')
    def _onchange_employee(self):
        if self.employee_id:
            self.name = self.employee_id.name
            self.job_positon = self.employee_id.job_title or ''
            self.depatement_id = self.employee_id.department_id.id
            self.phone = self.employee_id.work_phone or ''
            self.image = self.employee_id.image_1920 or False
        else:
            self.name = ''
            self.job_positon = ''
            self.depatement_id = False
            self.phone = ''
            self.image = False
