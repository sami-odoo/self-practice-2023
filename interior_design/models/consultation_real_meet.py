from odoo import fields,models,api

class Consultation_virtual_meet(models.Model):
    _name = "consultaion.real.meet"
    _description = "This is to have consultation in an offline meet"
    _rec_name="customer_name"
    _inherit = ['mail.thread', 'mail.activity.mixin',]

    customer_name = fields.Char(required=True)
    type_id = fields.Many2one("interior.design.property.type")
    property_painting = fields.Boolean(default=False)
    property_furnishing = fields.Boolean(default=False)
    date_availablity = fields.Date(copy=False,default=fields.date.today())
    painting_price = fields.Float(compute="_compute_painting")
    furnishing_price = fields.Float(compute="_compute_furnishing")
    total_cost = fields.Float(compute="_compute_total_cost",default=0)
    paint_colors = fields.Many2many("design.interior.paint")
    meeting_state = fields.Selection(copy=False,selection=[('new','NEW'),('generted','APPOINTMENT BOOKED'),('done','DONE'),('cancelled','APPOINTMENT CANCELLED')],default='new',tracking=True)
    consultant_id = fields.Many2one("interior.employee.dat")


    @api.depends('property_painting')
    def _compute_painting(self):
        # import pdb
        # pdb.set_trace()
        if self.property_painting:
            self.painting_price=500
        else:
            self.painting_price=0

    @api.depends('property_furnishing')
    def _compute_furnishing(self):

            if self.property_furnishing:
                self.furnishing_price=1000
            else:
                self.furnishing_price=0

    @api.depends('property_painting','property_furnishing')
    def _compute_total_cost(self):
                self.total_cost = self.furnishing_price + self.painting_price

    def perform_cancel(self):
        for record in self:
                record.meeting_state = 'cancelled'

    def perform_booking(self):
        for record in self:
            record.meeting_state = 'generted'
        
    # @api.model
    # def create(self, values):

    #     self.env['interior.employee.dat'].create(
    #         {
    #             'name': self.customer_name,
    #         },
    #     )

    #     return super().create(values)
