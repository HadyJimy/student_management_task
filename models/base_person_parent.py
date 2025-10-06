from odoo import models, fields, api, _

class BasePerson(models.AbstractModel):
    _name='base.person'
    _description="base person abstract model this is the main models"

    name = fields.Char(string='Name', required=True, index=True)
    age_custom = fields.Integer(string='Age', index=True)
    date_of_birth = fields.Date()
