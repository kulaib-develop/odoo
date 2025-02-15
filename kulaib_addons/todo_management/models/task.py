from odoo import models, fields, _
class Task(models.Model):
    _name = 'todo.task'
    _description = 'Task'
    _inherit = ['mail.thread','mail.activity.mixin']
    STATUS_TYPES = [
        ('new', _('New')),
        ('in_progress', _('In Progress')),
        ('completed', _('Completed')),
        ('closed', _('Closed')),
    ]
    name = fields.Char(required=True, tracking=1)
    assign_to_id = fields.Many2one('res.partner', tracking=1)
    description = fields.Text(tracking=1)
    due_date = fields.Date(tracking=1)
    status = fields.Selection(STATUS_TYPES, tracking=1,copy=False,default="new")
    active = fields.Boolean(default=True,copy=False)
    expected_complete_date = fields.Date(tracking=1)
    is_late = fields.Boolean()

    def action_closed(self):
        for rec in self:
            rec.status = 'closed'
    
    def _cron_check_complete_task_date(self):
        data = self.search([('expected_complete_date')])
        data.update({
            'is_late': True
        })