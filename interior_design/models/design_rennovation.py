from odoo import fields,models

class Design_rennovation(models.Model):
    _name="design.interior.rennovation"
    _description = "This is pasrt of interior design but for rennovation purpose"

    name = fields.Char(required=True)