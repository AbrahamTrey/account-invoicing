# -*- coding: utf-8 -*-
# Copyright 2004-2011 Pexego Sistemas Informáticos. (http://pexego.es)
# Copyright 2016 Antonio Espinosa <antonio.espinosa@tecnativa.com>
# Copyright 2014-2017 Pedro M. Baeza <pedro.baeza@tecnativa.com>
# Copyright 2017 Abraham Gonzalez (http:www.trey.es)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class AccountInvoiceLine(models.Model):
    _inherit = 'account.invoice.line'

    origin_line_ids = fields.Many2many(
        comodel_name='account.invoice.line',
        column1='refund_line_id',
        column2='original_line_id',
        relation='account_invoice_line_refunds_rel',
        string="Original invoice line",
        help="Original invoice line to which this refund invoice line "
             "is referred to")
    refund_line_ids = fields.Many2many(
        comodel_name='account.invoice.line',
        column1='original_line_id',
        column2='refund_line_id',
        relation='account_invoice_line_refunds_rel',
        string="Refund invoice line",
        help="Refund invoice lines created from this invoice line")
