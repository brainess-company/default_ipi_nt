from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.model
    def create(self, vals):
        # Busca o imposto IPI NT
        ipi_nt_tax = self.env['account.tax'].search([
            ('name', '=', 'IPI NT'),  # Substitua pelo nome exato do imposto
            ('type_tax_use', '=', 'sale'),  # Certifique-se de que é um imposto de venda
        ], limit=1)
        if ipi_nt_tax:
            vals['ipi_tax_id'] = ipi_nt_tax.id
        return super(SaleOrderLine, self).create(vals)
