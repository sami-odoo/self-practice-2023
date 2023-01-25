from odoo import api,fields,models

class Types_of_property(models.Model):
    _name="interior.design.property.type"
    _description = "Just to define the type of property"


    name=fields.Char(required=True)