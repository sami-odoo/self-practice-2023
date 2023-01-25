from odoo import fields,models

class Customer_info(models.Model):
    _name="customer.info"
    _description="This is for customer information"
    _inherit = ['mail.thread', 'mail.activity.mixin',]

    name=fields.Char(required=True)
    price=fields.Float(required=True)
    emp_id = fields.Many2one("interior.employee.dat")
    work_done = fields.Selection(selection=[('paint','Paint'),('furniture','Furniture'),('both','Paint and Furniture')])