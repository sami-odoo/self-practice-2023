from odoo import fields,models


class Rennovation_stories(models.Model):
    _name="rennovation.stories"
    _description = "This is to see the reviews of our beloved customers"


    name=fields.Char()
    review = fields.Text()
    