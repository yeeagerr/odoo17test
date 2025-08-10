from odoo import models, fields, api
from datetime import date
from odoo.exceptions import ValidationError

class purchase_learn(models.Model):
    _name = "purchase.learn"

    def func_delete_status_draft(self):
        purchase_learn_obj = self.env['purchase.learn'].search([('status', '=', 'draft')])
        for line in purchase_learn_obj:
             line.unlink()
        return True

    def func_approved(self):
        if self.status == "draft":
            if self.name == "New":
                seq = self.env["ir.sequence"].next_by_code("purchase.learn") or "New"
                self.name = seq
            self.status = "approve"


    def func_set_done(self):
        if self.status == "approve":
            self.status = "done"

    
    @api.model
    def create(self, values):
        res = super(purchase_learn, self).create(values)
        for rec in res:
            tanggal_purchase = rec.tanggal
            tanggal_sekarang = date.today()
            if tanggal_purchase < tanggal_sekarang:
                raise ValidationError("Tanggal Purchase Tidak Boleh Kurang Dari Tanggal Sekarang")
            return res

    
    def write(self, values):
        res = super(purchase_learn, self).write(values)
        if 'tanggal' in values:
            tanggal_purchase = self.tanggal
            tanggal_sekarang = date.today();
            if tanggal_purchase < tanggal_sekarang:
                raise ValidationError(("Tanggal Purchase Tidak Boleh Kurang Dari Tanggal Sekarang"))
            return res
    
    name = fields.Char(string="Nama", required=True, default="New")
    tanggal = fields.Date(string="Tanggal")
    status = fields.Selection([("draft", "Draft"), ("approve", "Approve"), ("done", "Done")], default="draft")
    purchase_learn_ids = fields.One2many("purchase.learn.line", 'purchase_learn_id', string="Purchase Learn IDS")
    brand_ids = fields.Many2many("brand.learn", "purchase_learn_brand_rel", 'purchase_learn_id', 'brand_id', string="Brand")


class purchase_learn_line(models.Model):
    _name = "purchase.learn.line"

    @api.onchange('product_id')
    def func_onchange_product_id(self):
        if not self.product_id:
            return {}
        else:
            self.description = self.product_id.name
        return{}


    def _func_subtotal(self):
        for line in self:
            line.subtotal = line.quantity * line.price
    
    
    purchase_learn_id = fields.Many2one("purchase.learn", string="Purchase Learn ID")
    product_id = fields.Many2one('product.product', string="Product ID")
    quantity = fields.Float(string="Quantity", default=0)
    uom_id = fields.Many2one('uom.uom', string="Satuan")
    description = fields.Char(string="Description")
    price = fields.Float(string="Price", default=0.0)
    subtotal = fields.Float(string="Sub Total", compute=_func_subtotal)


class brand_learn(models.Model):
    _name = "brand.learn"

    name = fields.Char(string="name")


class purchase_learn_report_wizard(models.TransientModel):
    _name = "purchase.learn.report.wizard"

    name = fields.Char(string="Name")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")