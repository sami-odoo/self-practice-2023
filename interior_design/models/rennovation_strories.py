from odoo import fields,models


class Rennovation_stories(models.Model):
    _name="rennovation.stories"
    _description = "This is to see the reviews of our beloved customers"


    name=fields.Char()
    review = fields.Text()
    rating = fields.Selection(copy=False,selection=[('0','Very Low'),('1','Low'),('2','Average'),('3','Good'),('4','Very Good'),('5','Best')])
    image = fields.Image(string='Image')
    