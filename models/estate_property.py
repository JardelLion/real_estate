from odoo import models, fields


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = 'The description of Estate property'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    postcode = fields.Char(string='Postcode')
    date_availability = fields.Date()
    expected_price = fields.Float(string='Expected price', required=True)
    selling_price = fields.Float(string='Selling price')
    bedrooms = fields.Integer(string='Bedrooms')
    living_area = fields.Integer(string='Living area')
    facades = fields.Integer(string='Facades')

    garage = fields.Boolean(string='Garage')
    garden = fields.Boolean(string="Garden")
    garden_area = fields.Integer(string='Garden Area')
    garden_orientation = fields.Selection([('north', 'North'),
                                           ('south', 'South'),
                                           ('west', 'West')])














