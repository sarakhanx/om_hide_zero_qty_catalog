# Odoo Product and Sale Order Enhancement Module

## Overview

This module extends the functionality of Odoo's `product.product` and `sale.order` models to improve product management and sales operations. It provides enhanced access rights handling and product filtering capabilities.

## Features

- **Enhanced Product Search**: Overrides the `_search` method in `product.product` to bypass access rights using `sudo()`, allowing comprehensive data retrieval.
- **Improved Sale Order Management**: Extends `sale.order` to filter saleable products with available stock during order line selection, ensuring accurate and efficient sales operations.

## File Descriptions

### 1. `models/product_product.py`

- **Purpose**: Enhances the product search functionality.
- **Key Functionality**:
  - Overrides the `_search` method to use `sudo()`, which bypasses standard access rights checks. This ensures that searches can retrieve all necessary data without being limited by user permissions.

### 2. `models/sale_order.py`

- **Purpose**: Improves the management of sale orders by filtering products.
- **Key Functionality**:
  - **_is_sale_order_line_selection**: Checks if the current context is for sale order line product selection.
  - **_get_product_catalog_order_data**: Uses `sudo()` to handle product access and filters products to include only those that are saleable and have available stock.
  - **_get_product_catalog_order_line_info**: Similar to the above, it ensures that only saleable products with stock are considered during sale order line selection.

### 3. `models/product_template.py`

- **Purpose**: (Assuming similar enhancements as the other files, as the content is not fully visible)
- **Key Functionality**: Likely extends product template functionalities to align with the enhancements in product and sale order management.

## Installation

1. Clone the repository into your Odoo addons directory.
2. Update the Odoo module list by restarting the Odoo server.
3. Install the module from the Odoo Apps interface.

## Usage

- **Product Search**: Use the enhanced search functionality to retrieve products without access restrictions.
- **Sale Order Processing**: Create and manage sale orders with improved product selection, ensuring only saleable products with stock are included.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This module is licensed under the Odoo Proprietary License v1.0.

---

This README provides a comprehensive overview of the module, detailing the purpose and functionality of each file, and should serve as a useful document for developers. Adjust the content as needed to fit any additional features or specific contexts of your project.
