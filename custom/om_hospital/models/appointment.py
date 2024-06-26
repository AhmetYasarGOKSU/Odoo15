from odoo import api, fields, models, _


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Hospital Appointment"

    name = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,
                       default=lambda self: _('New'))

    note = fields.Text(string='Description')
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'), ('done', 'Done'), ('cancel', 'Cancelled')],
                             default="draft", tracking=True, string="Status")
    patient_id = fields.Many2one('res.partner', string="Responsible")

    def action_confirm(self):
        self.state = 'confirm'

    def action_done(self):
        self.state = 'done'

    def action_draft(self):
        self.state = 'draft'

    def action_cancel(self):
        self.state = 'cancel'

    @api.model
    def create(self, vals):
        if not vals.get('note'):
            vals['note'] = "New Patient"
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code("hospital.appointment") or _("New")
        res = super(HospitalAppointment, self).create(vals)
        return res
