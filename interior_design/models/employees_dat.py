from odoo import api,models,fields

class Employees_data(models.Model):
    _name="interior.employee.dat"
    _description = "This is basically to get the information about the employee"

    name=fields.Char()
    tag_id = fields.Many2one("employee.tag")
    appointment_ids = fields.One2many("consultaion.real.meet","consultant_id")
    online_appointment_ids = fields.One2many("consultaion.virtual.meet","consultant_id")
    
