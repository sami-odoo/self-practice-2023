#-*- coding -*-

from odoo import fields,models

class Interior_desigining(models.Model):
    _name="design.interior"
    _description="App for interior designing"
    _inherit = ['mail.thread', 'mail.activity.mixin',]



    name = fields.Char(required=True)
    phone_no = fields.Char(required=True) 
    c_email = fields.Char()
    c_end_date = fields.Date()
    h_no = fields.Char()
    h_block = fields.Char()
    society_name = fields.Char()
    h_area = fields.Char()
    h_city = fields.Char()
    h_state = fields.Char()
    h_pin = fields.Char()
    work_state = fields.Selection(copy=False,selection=[('new','NEW'),('measurements','Measurements'),('designing','Designing'),('painting','Painting'),('furnishing','Furnishing'),('cleaning','Cleaning'),('cancelled','Cancelled')],default='new',tracking=True)

    # Relational Fields
    property_type_id = fields.Many2one("interior.design.property.type")


    # actions
    def perform_assing(self):

        for record in self:
            record.work_state = "measurements"

    def perform_cancel(self):

        for record in self:
            record.work_state = "cancelled"
    