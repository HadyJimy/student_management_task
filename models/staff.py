from odoo import models, fields

class Teacher(models.Model):
    _name = 'staff.staff'
    _inherit = 'base.person'

    name = fields.Char(string='Name')
    position = fields.Char(string='Position')
    salary=fields.Float()
    user_id = fields.Many2one('res.users', string='Related User')  # link to a user to send notifications
