from odoo import api,models,fields

class Customer_relations_with_company(models.Model):
    _name="customer.relation.company"
    _description = "Defines the type of relation customer has with company"

    name = fields.Char(required=True)
    