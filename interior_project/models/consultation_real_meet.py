from odoo import fields,models,Command

class Inheriting_consultation_real(models.Model):
    _inherit = "consultaion.real.meet"

    def perform_booking(self):
        self.env['project.project'].create({
            'name': 'Consultation',
            'task_ids': [
                Command.create({
                    'name': 'Real Meet',
                })
            ]
        })
        return super().perform_booking()
    

