from odoo import models, api
import logging

_logger = logging.getLogger(__name__)

class ProductProduct(models.Model):
    _inherit = 'product.product'

    @api.model
    def _search(self, domain, offset=0, limit=None, order=None, access_rights_uid=None):
        """Override search to handle access rights"""
        return super(ProductProduct, self.sudo())._search(
            domain, offset=offset, limit=limit, order=order,
            access_rights_uid=access_rights_uid
        ) 