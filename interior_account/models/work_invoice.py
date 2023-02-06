from odoo import api,fields,Command,models

class Create_invo(models.Model):
    _inherit = "design.interior"

    # inheriting assign function
    def perform_assing(self):

        for record in self:
            self.env['account.move'].sudo().create({
                'move_type': 'out_invoice',
                'invoice_date': '2023-01-28',
                'name': 'Design Invoicing Report Inherit',
                'invoice_line_ids': [
                    Command.create({
                        'name': 'Paint',
                        'price_unit': 2000,
                        'quantity': 1,
                    }),
                    Command.create({
                        'name': 'Administration fees',
                        'price_unit': 100,
                        'quantity': 1,
                    }),
                ],
         
            })
        return super().perform_assing()