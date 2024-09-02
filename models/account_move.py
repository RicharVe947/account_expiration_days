# Copyright 2022 Munin
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
import datetime

from odoo import api, fields, models
from datetime import date


class AccountMove(models.Model):
    _inherit = "account.move"
    
    new_expiration_date = fields.Date(string='Real Due Date', compute="_compute_new_expiration_date", store=True)
    debit_note_status = fields.Selection([
        ('unmatured', 'Unmatured'),
        ('on_note', 'Process Debit Note')],
        string="Debit note", readonly=False, required=True, default='unmatured', tracking=True, store=True)
    debit_note_status_manual = fields.Boolean(default=False)
    
    @api.onchange('debit_note_status')
    def _manual_change_debit_note_status(self):
        self.debit_note_status_manual = True
    
    @api.depends('invoice_date_due')
    def _compute_new_expiration_date(self):
        for record in self:
            date_ref = record.invoice_date_due or record.date
            if date_ref and record.invoice_payment_term_id:
                date_ref = date_ref + datetime.timedelta(days=record.invoice_payment_term_id.extension_credit_days)
            record.new_expiration_date = date_ref

    def _compute_debit_note_required(self):
        for record in self.env['account.move'].search([('move_type', '=', 'out_invoice')]):
            if record.new_expiration_date:
                date_ref = record.new_expiration_date
                diff_days = date.today() - date_ref
                diff_days = diff_days.days
                if record.debit_note_status_manual:
                    
                    record.debit_note_status = record.debit_note_status
                else:
                    record.debit_note_status = 'unmatured' if diff_days <= 0 else 'on_note'
            else:
                record.debit_note_status = 'unmatured'
