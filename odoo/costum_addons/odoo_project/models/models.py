# -*- coding: utf-8 -*-

from odoo import models, fields, api


class OdooProject(models.Model):
    _name = 'odoo.project'
    _description = 'Odoo Project'
    _inherit = ["odoo.project.abstract", "mail.thread"]

    name = fields.Char(string="Name",default="New" , index=True)
    total = fields.Integer(string="Total", tracking=True)
    description = fields.Text(string="Description")
    user_id = fields.Many2one(comodel_name='res.users', string="User", tracking=True)
    total_compute = fields.Float(compute="_compute_total", store=True, string="Total Compute", tracking=True)

    # comodel bisa di cari di technical lalu ke model
    # relation untuk nama dari table pivot
    # column 1 nama column id dari OdooProject
    # column 2 nama column id dari pihak lain yang direlasikan
    tags_ids = fields.Many2many(
        comodel_name="res.partner.category", 
        relation="odoo_project_res_partner_category_rel", column1="odoo_project_id", column2="res_partner_category_id", string="Partner Tags"
        )
    
    # Kalau one 2 many harus ada table yang menerima one2many ini, kalau ini di deklarasi disini
    # maka ini akan seperti, 1 odoo_project_line memiliki banyak dari table yang dituju
    odoo_project_line = fields.One2many(comodel_name="odoo.project.line", inverse_name="odoo_project_id", string="Odoo Project")
    
    # Kalau store false maka tidak akan ada di database
    active = fields.Boolean(string="Active", store=True)
    company_id = fields.Many2one(comodel_name="res.company", string="Company", tracking=True)

    currency_id = fields.Many2one(comodel_name="res.currency", string="Currency")

    # float yang di embeed dengan currency symbol (secara ui saja sebenarnya)
    price_total = fields.Monetary(
        compute="_compute_total",
        store=True,
        string="Price Total",
        currency_field="currency_id", tracking=True
    )

    attachment = fields.Binary(string="Attachment")
    icon_image = fields.Image(string="Icon", max_height=1024, max_width=1024)

    # sama seperti text, tapi bedanya bisa di bold, italic dll...
    note = fields.Html(string="Note")
    date_only = fields.Date(string="Date only", default=fields.Date.today())
    start_date = fields.Datetime(string="Start Date", default=fields.Datetime.today())
    end_date = fields.Datetime(string="End Date", default=fields.Datetime.today())
    state = fields.Selection(
        selection=[("draft", "Draft"),
        ("ready", "Ready"),
        ("done", "Done"),
        ("cancel", "Cancel"),],
        string="Status", default="draft", required=True, tracking=True
    )
    ref = fields.Reference(string="Reference", selection=[("res.partner", "Partner")])
    model_name = fields.Char(string="Model") # odoo.tutorial
    res_id = fields.Many2oneReference(string="Res ID", model_name="model_name")

    @api.depends('total')
    def _compute_total(self):
        for record in self:
            record.total_compute = float(record.total) / 100
            record.price_total = record.total_compute

    def action_ready(self):
        if(self.state) == 'draft':
            self.state = 'ready'
    
    def action_done(self):
        if self.state == 'ready':
            self.state = 'done'    
    
    
    def action_cancel(self):
        if self.state == 'ready':
            self.state = 'cancel'

    
    # ada yang single ada yang multi, bedanya kalau multi gaperlu di loop isi data banyak
    @api.model_create_multi
    def create(self, vals_list):
        res = super(OdooProject, self).create(vals_list)
        return res
        
    
    def read(self, fields=None, load='_classic_read'):
        return super().read(fields=fields, load=load)
    

    def write(self, vals):
        res = super().write(vals)
        return res
    

    def unlink(self):
        
        return super.unlink()


class odooProjectLine(models.Model):
    _name="odoo.project.line"

    # ondelete, null, restrict, cascade
    # null kalau record base tabel (odoo.project) dihapus, maka semua yang bersangkutan akan null
    # restrict kena blocking
    # cascade bakal kehapus yang bersangkutan
    name = fields.Char(string="Name")
    qty = fields.Float(default=0)
    price_unit = fields.Float(default=0)
    odoo_project_id = fields.Many2one(comodel_name="odoo.project", string="Odoo Project", ondelete="cascade")


class OdooModelAbstract(models.AbstractModel):
    _name = 'odoo.model.abstract'
    _description = 'Odoo Model Abstract Odoo Porject'