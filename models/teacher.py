from odoo import models, fields,api,_
from odoo.exceptions import ValidationError
class Teacher(models.Model):
    _name = 'teacher.teacher'
    _inherit = ['base.person', 'mail.thread', 'mail.activity.mixin']

    subject = fields.Char(string='Subject',index=1)
    user_id = fields.Many2one('res.users', string='Related User')  # link to a user to send notifications
    active = fields.Boolean(default=True, tracking=True)


    @api.model
    def create(self, vals):
        """Override create to:
        1. Post a chatter message when a teacher is created.
        2. Demonstrate how to use super() properly.
        """
        # Always call super() first to let Odoo ORM handle creation safely
        record = super(Teacher, self).create(vals)

        # Example of automatic chatter message
        record.message_post(
            body=_("🎓 A new teacher <b>%s</b> has been created with subject <b>%s</b>.") %
                 (record.name, record.subject)
        )

        # Optional: assign a default user or notify admins
        if not record.user_id:
            admin_user = self.env.ref('base.user_admin', raise_if_not_found=False)
            if admin_user:
                record.user_id = admin_user
                record.message_post(
                    body=_("Assigned automatically to admin user for follow-up.")
                )

        return record

    def write(self, vals):
        """Override write to log changes in chatter."""
        res = super(Teacher, self).write(vals)
        for rec in self:
            rec.message_post(body=_("Teacher record updated."))
        return res

    # ----------------------------------------------------------
    # CONSTRAINTS & VALIDATIONS
    # ----------------------------------------------------------

    @api.constrains('age')
    def _check_age_limit(self):
        """Ensure teacher age is within reasonable limits."""
        for rec in self:
            if rec.age and (rec.age < 18 or rec.age > 70):
                raise ValidationError(
                    _("Teacher age must be between 18 and 70 years.")
                )

    # ----------------------------------------------------------
    # BUSINESS LOGIC
    # ----------------------------------------------------------

    def action_notify_courses(self):
        """Notify via chatter about all courses the teacher handles."""
        for rec in self:
            if rec.course_ids:
                course_names = ", ".join(rec.course_ids.mapped('name'))
                rec.message_post(
                    body=_("This teacher currently handles the following courses: %s.") % course_names
                )
            else:
                rec.message_post(body=_("No assigned courses yet."))