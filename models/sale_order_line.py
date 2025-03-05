from odoo import models, fields, api
from odoo.tests.common import Form
import logging

_logger = logging.getLogger(__name__)

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    def write(self, vals):
        ipi_nt_tax = self.env['account.tax'].search([
            ('name', '=', 'IPI NT'),
            ('type_tax_use', '=', 'sale'),
        ], limit=1)

        _logger.info("ipi_nt_tax = ", ipi_nt_tax)

        for record in self:
            with Form(record) as line_form:
                for key, value in vals.items():
                    setattr(line_form, key, value)
                if ipi_nt_tax:
                    line_form.ipi_tax_id = ipi_nt_tax
                line_form.save()
        return True
