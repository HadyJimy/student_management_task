from odoo import models, fields, api

class UnifiedPersonSearch(models.TransientModel):
    _name = 'unified.person.search'
    _description = 'Unified Search for Student, Teacher, and Staff,Course'

    search_term = fields.Char(string='Search Term', required=True)
    result_ids = fields.One2many(
        'unified.person.result',
        'search_id',
        string='Search Results'
    )

    def action_search(self):
        """Perform unified search and store results temporarily."""
        self.ensure_one()
        term = self.search_term
        domain = [('name', 'ilike', term)]

        results = []

        # Collect from all 3 models
        for model_name, role in [
            ('student.student', 'Student'),
            ('teacher.teacher', 'Teacher'),
            ('teacher.teacher', 'Teacher'),
            ('course.course', 'Course')
        ]:
            for record in self.env[model_name].search(domain, limit=50):
                results.append({
                    'name': record.name,
                    'role': role,
                    'related_model': model_name,
                    'related_id': record.id,
                    'search_id': self.id,
                })

        # Clear old results
        self.result_ids.unlink()
        self.env['unified.person.result'].create(results)

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'unified.person.search',
            'view_mode': 'form',
            'res_id': self.id,
            'target': 'new',
        }


class UnifiedPersonResult(models.TransientModel):
    _name = 'unified.person.result'
    _description = 'Unified Search Result'

    name = fields.Char(string='Name', index=True)
    role = fields.Char(string='Role')
    related_model = fields.Char(string='Model Name')
    related_id = fields.Integer(string='Record ID')
    search_id = fields.Many2one('unified.person.search', string='Search Ref', ondelete='cascade')
