from odoo import models, fields

class GuestBook(models.Model):
    _name="guest.book"
    _description="Guest Book"

    name = fields.Char(string="Nama Kamu", required=True)
    company = fields.Char(string='Perusahaan/Instansi')
    purpose = fields.Text(string='Keperluan')
    checkin = fields.Datetime(string='Waktu Datang', default=fields.Datetime.now)