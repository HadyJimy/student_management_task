from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Course(models.Model):
    _name = 'course.course'
    _description = 'Course'

    # The Main that tells datebase to craete index attribute on this column to make it more unique
    name = fields.Char(string='Name', required=True, index=True)
    description = fields.Text(string='Description')
    teacher_id = fields.Many2one('teacher.teacher', string='Teacher', required=False)
    staff_id = fields.Many2one('staff.staff', string='Responsible Staff')
    student_id = fields.Many2one('student.student')
    student_ids = fields.Many2many(
        'student.student',
        'course_student_rel',
        'course_id',
        'student_id',
        string='Students'
    )

    average_age = fields.Float(string='Average Age', compute='_compute_average_age', store=True)

    # This Mean That there is the more strongest level of security on this field this is database level
    @api.constrains('teacher_id')
    def _check_teacher_assigned(self):
        # This constraint prevents a Course from being created without a teacher.
        for rec in self:
            if not rec.teacher_id:
                raise ValidationError('Course must have an teacher.')
    # This mean when the field age of student change i ll calculate to get the average and add it in this field average_age
    # I make this field because this depend on specific field
    @api.depends('student_ids.age')
    def _compute_average_age(self):
        for rec in self:
            if rec.student_ids:
                ages = [s.age for s in rec.student_ids if s.age is not None]
                rec.average_age = sum(ages) / len(ages) if ages else 0.0
            else:
                rec.average_age = 0.0
