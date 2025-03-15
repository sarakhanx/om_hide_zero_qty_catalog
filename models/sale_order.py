from odoo import models, api
import logging

_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _is_sale_order_line_selection(self):
        """Check if current context is for sale order line product selection"""
        return (self.env.context.get('active_model') == 'sale.order' and 
                self._context.get('catalog_mode', '') == 'order_line')

    def _get_product_catalog_order_data(self, products, **kwargs):
        """Override to handle product access with sudo and filter saleable products"""
        # Use sudo() for the entire operation
        self = self.with_company(self.company_id).sudo()
        products = products.sudo()
        
        # Only filter in sale order line selection context
        if self._is_sale_order_line_selection():
            products = products.filtered(lambda p: p.sale_ok and p.qty_available > 0)
        return super()._get_product_catalog_order_data(products, **kwargs)

    def _get_product_catalog_order_line_info(self, product_ids=None, **kwargs):
        """Override to handle product access with sudo"""
        # Use sudo() for the entire operation
        self = self.with_company(self.company_id).sudo()
        ProductProduct = self.env['product.product'].sudo()
        
        # If no product_ids provided and in sale order line context
        if product_ids is None and self._is_sale_order_line_selection():
            domain = [('sale_ok', '=', True)]
            if self._is_sale_order_line_selection():
                domain.append(('qty_available', '>', 0))
            products = ProductProduct.search(domain)
            product_ids = products.ids
            
        result = super()._get_product_catalog_order_line_info(product_ids=product_ids, **kwargs)
        
        # Filter products only in sale order line context
        if result and 'products' in result and self._is_sale_order_line_selection():
            products = result.get('products', [])
            if products:
                if isinstance(products, list):
                    product_ids = [p.get('id') for p in products if isinstance(p, dict) and p.get('id')]
                    products = ProductProduct.browse(product_ids)
                else:
                    products = ProductProduct.browse(products.ids)
                
                # Filter saleable products with stock
                filtered_products = products.filtered(lambda p: p.sale_ok and p.qty_available > 0)
                result['products'] = filtered_products
                
        return result 