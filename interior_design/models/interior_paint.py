from odoo import api,models,fields

class Interior_paints(models.Model):
    _name="design.interior.paint"
    _description = "List of colors for painting interior"

    name=fields.Char(required=True)
    color = fields.Integer()
    