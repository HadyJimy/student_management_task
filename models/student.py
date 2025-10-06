from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import date

class Student(models.Model):
    _name = 'student.student'
    _inherit = 'base.person'

    document = fields.Binary(string='Documents')
    course_ids = fields.Many2many(
        'course.course',
        'course_student_rel',
        'student_id',
        'course_id',
        string='Courses'
    )
    course_id = fields.Many2one('course.course', string='Course')
    # company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company.id)

    @api.model
    def create(self, vals):
        # When overriding create, always call super() to keep Odoo lifecycle (create constraints, automated actions etc).
        record = super().create(vals)
        if record.age==0:
            raise ValidationError(_('Age must be more than 0.'))

        if record.age:
            if not (18 <= record.age <= 60):
                # If requirement fails, raise validation error.
                raise ValidationError(_('Age must be between 18 and 60.'))
        # Trigger notification to teacher if student assigned to course (we also support automated action alternative)
        for student in record:
            # Ensure course and teacher exist
            if student.course_id and student.course_id.teacher_id:
                teacher = student.course_id.teacher_id
                # Post message to teacher’s chatter
                teacher.message_post(
                    body=_("🎓 A new student <b>%s</b> has registered in your course <b>%s</b>.") % (
                        student.name, student.course_id.name),
                    subject=_("New Student Registered"),
                    subtype_xmlid="mail.mt_comment",
                )
        return record

    @api.depends('date_of_birth')
    def _compute_age_from_dob(self):
        for rec in self:
            if rec.date_of_birth:
                today = date.today()
                years = today.year - rec.date_of_birth.year
                rec.age = years
            else:
                rec.age = 0

    age = fields.Integer(string='Age', compute='_compute_age_from_dob', store=True)
