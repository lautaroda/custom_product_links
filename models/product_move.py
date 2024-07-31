# models/product_move.py
from odoo import models, fields

class StockMove(models.Model):
    _inherit = 'stock.move'

    related_document_link = fields.Char(string="Enlace al Documento Relacionado", compute="_compute_related_document_link")

    def _compute_related_document_link(self):
        for record in self:
            if record.picking_id.purchase_id:
                record.related_document_link = record.picking_id.purchase_id.get_portal_url()
            elif record.picking_id.sale_id:
                record.related_document_link = record.picking_id.sale_id.get_portal_url()
            else:
                record.related_document_link = ''

    def open_related_document(self):
        self.ensure_one()
        if self.related_document_link:
            return {
                'type': 'ir.actions.act_url',
                'url': self.related_document_link,
                'target': 'new',
            }
