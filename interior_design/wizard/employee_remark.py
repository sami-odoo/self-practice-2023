from odoo import fields,models

class Employee_Remark(models.TransientModel):
    _name = "employee.remark"
    _description = "Employee can send remark and discount coupons to customer"


    remarks = fields.Text(required=True)
    discount = fields.Float()
    