from odoo import models,fields

class Employee_tags(models.Model):
    _name="employee.tag"
    _description = "How good is the employee"

    name=fields.Char(required=True)
    color = fields.Integer()