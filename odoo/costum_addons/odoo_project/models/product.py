# Mengimpor field dan model dari framework Odoo
from odoo import fields, models

# Membuat class yang mewarisi model 'product.template' milik Odoo
class ProductTemplate(models.Model):
    # Memberitahu Odoo bahwa kita ingin menambahkan (inherit) dari model 'product.template'
    _inherit = 'product.template'

    # Menambahkan field baru bernama 'custom_barcode' ke model produk
    # Bertipe Char (teks pendek) dan akan tampil di form dengan label "Custom Barcode"
    custom_barcode = fields.Char()

    # Method untuk mengisi ulang field 'custom_barcode' dengan nilai yang sama (dari field itu sendiri)
    # Biasanya dipakai jika field ini digenerate dari proses logika tertentu
    def GenerateCustomBarcode(self):
        # Menulis ulang field 'custom_barcode' dengan nilainya sendiri
        # ⚠️ Efeknya di sini tidak terlihat jelas karena isinya tidak berubah
        return self.write({'custom_barcode': self.custom_barcode})
