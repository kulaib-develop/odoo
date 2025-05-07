from odoo import models, fields, _, api
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
    assign_to_email = fields.Char(related='assign_to_id.email')
    description = fields.Text(tracking=1)
    due_date = fields.Date(tracking=1)
    status = fields.Selection(STATUS_TYPES, tracking=1,copy=False,default="new")
    active = fields.Boolean(default=True,copy=False)
    expected_complete_date = fields.Date(tracking=1)
    is_late = fields.Boolean()
    subtask_ids = fields.One2many('todo.subtask','task_id')
    total_subtasks = fields.Integer(compute="_total_subtasks")
    
    def action_closed(self):
        for rec in self:
            rec.status = 'closed'
    
    def _cron_check_complete_task_date(self):

        data = self.search([('expected_complete_date','<=',fields.Date.today())])
        data.update({
            'is_late': True
        })
    @api.depends('subtask_ids')
    def _total_subtasks(self):
        for rec in self:
            rec.total_subtasks = len(rec.subtask_ids)

class SubTask(models.Model):
    _name='todo.subtask'
    _description = "SubTask"

    name = fields.Char(required=True)
    start = fields.Date()
    end = fields.Date()
    task_id = fields.Many2one('todo.task')