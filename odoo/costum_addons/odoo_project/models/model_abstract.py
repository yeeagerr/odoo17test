from odoo import fields, models

class ModelAbstract(models.AbstractModel):
    _name="odoo.project.abstract"
    _description="Abstract model of odoo project"

    # Model yang inherit kesini akan tertambah data ini
    general_description = fields.Text()
    instructur_id = fields.Many2one(
        comodel_name="res.users",
        string="instructur",
        ondelete="restrict",
    )

    # Model yang inherit ke sini dapat menggunakan function ini tanpa mengubah kode asli model ini
    def _custom_abstract_model(self):
        return
