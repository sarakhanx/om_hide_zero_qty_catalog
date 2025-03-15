from odoo import models, fields, api
from odoo.tools import float_round, float_is_zero
from odoo.exceptions import UserError
import logging

_logger = logging.getLogger(__name__)
DEFAULT_ROUNDING = 0.01

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def _get_safe_rounding(self):
        """Get a safe rounding value, never returning 0"""
        self.ensure_one()
        rounding = self.uom_id.rounding if self.uom_id else DEFAULT_ROUNDING
        return rounding if rounding > 0 else DEFAULT_ROUNDING

    @api.depends('qty_available')
    def _compute_quantities(self):
        """Override to ensure proper rounding"""
        for template in self.sudo():
            try:
                super(ProductTemplate, template)._compute_quantities()
                if hasattr(template, 'qty_available'):
                    rounding = template._get_safe_rounding()
                    if template.qty_available is not False:
                        template.qty_available = float_round(
                            template.qty_available,
                            precision_rounding=rounding
                        )
            except Exception as e:
                template.qty_available = 0.0
                _logger.error("Error computing quantities for product %s: %s", template.display_name, str(e))

    @api.model
    def _search_qty_available(self, operator, value):
        """Search method for qty_available with proper error handling"""
        domain = []
        if not operator or value is None:
            return domain

        try:
            products = self.sudo().search([])
            product_ids = []
            
            for product in products:
                try:
                    rounding = product._get_safe_rounding()
                    qty = float_round(product.sudo().qty_available or 0.0, precision_rounding=rounding)
                    
                    if float_is_zero(qty, precision_rounding=rounding):
                        qty = 0.0
                    
                    if operator == '>' and qty > value:
                        product_ids.append(product.id)
                    elif operator == '<' and qty < value:
                        product_ids.append(product.id)
                    elif operator == '>=' and qty >= value:
                        product_ids.append(product.id)
                    elif operator == '<=' and qty <= value:
                        product_ids.append(product.id)
                    elif operator == '=' and float_is_zero(qty - value, precision_rounding=rounding):
                        product_ids.append(product.id)
                except Exception as e:
                    _logger.error("Error processing product %s: %s", product.display_name, str(e))
                    continue
                    
            domain = [('id', 'in', product_ids)]
        except Exception as e:
            _logger.error("Error in _search_qty_available: %s", str(e))
            
        return domain 