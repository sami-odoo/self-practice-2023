from odoo import models,fields,api

class Creating_event(models.Model):
    _inherit = "consultaion.real.meet"
    _description = "This is for event creation"

    # def perform_booking(self):
    #     self.env['calendar.event'].create([
    #             {'attendee_ids': [(0, 0, {'partner_id': self.id})],
    #             'name': 'Meeting for %s' % self.customer_name,
    #             'start': datetime.today(),
    #             'stop': datetime.today()+relativedelta(months=3),
    #             }
    #         ])


