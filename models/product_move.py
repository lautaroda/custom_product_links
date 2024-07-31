from odoo import models, fields, api

class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    related_document_link = fields.Char(string="Enlace al Documento Relacionado", compute="_compute_related_document_link")

    @api.depends('move_id.origin')
    def _compute_related_document_link(self):
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        for line in self:
            if line.move_id.origin:
                if line.move_id.origin.startswith('P'):
                    purchase_order = self.env['purchase.order'].search([('name', '=', line.move_id.origin)], limit=1)
                    if purchase_order:
                        line.related_document_link = f"{base_url}/web#id={purchase_order.id}&model=purchase.order&view_type=form"
                elif line.move_id.origin.startswith('S'):
                    sale_order = self.env['sale.order'].search([('name', '=', line.move_id.origin)], limit=1)
                    if sale_order:
                        line.related_document_link = f"{base_url}/web#id={sale_order.id}&model=sale.order&view_type=form"
                else:
                    line.related_document_link = ''
            else:
                line.related_document_link = ''
