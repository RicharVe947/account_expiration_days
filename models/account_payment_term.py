# Copyright 2022 Munin
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
import datetime

from odoo import api, fields, models


class AccountPaymentTerm(models.Model):
    _inherit = "account.payment.term"

    extension_credit_days = fields.Integer(default=7, string="Extension credit days" )