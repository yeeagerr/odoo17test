from odoo import models, fields

class LaptopScreen(models.Model):
    _name="laptop.screen"
    _description="Laptop Screen"

    screen_type = fields.Selection(selection=[
        ("va", "VA"), ("tn", "TN"), ("ips", "IPS"), ("amoled", "Amoled")
    ], default="ips", required=True)
    width = fields.Float(string="Width (inch)")
    height = fields.Float(string="Height (inch)")
    framerate = fields.Integer(string="Frame Rate (Hz)")


class LaptopLaptop(models.Model):
    _name="laptop.laptop"
    _description="laptop's"
    # ada treatment khusus, ketika model ini dibuat record baru nanti target model juga terbuat record nya
    _inherits={"laptop.screen" : "screen_id"}

    name = fields.Char(string="Laptop Name")
    screen_id = fields.Many2one(comodel_name="laptop.screen",string="Screen" ,auto_join=True, ondelete="cascade", index=True, required=True)
    fingerprint = fields.Boolean(string="Has Fingerprint ?")
    camera = fields.Boolean(string="Has Camera ?")
    cpu_discrete = fields.Boolean(string="Discrete VGA ?")
    cpu_onboard = fields.Boolean(string="Onboard VGA ?")
    cpu_core = fields.Integer(default=0)
    cpu_thread = fields.Integer(default=0)