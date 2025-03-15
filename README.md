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

---

Here's the detailed README with both English and Thai descriptions:

---

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

# โมดูลการปรับปรุงสินค้าและคำสั่งซื้อขายของ Odoo

## ภาพรวม

โมดูลนี้ขยายความสามารถของโมเดล `product.product` และ `sale.order` ของ Odoo เพื่อปรับปรุงการจัดการสินค้าและการดำเนินการขาย โดยให้การจัดการสิทธิ์การเข้าถึงและความสามารถในการกรองสินค้าที่ดีขึ้น

## คุณสมบัติ

- **การค้นหาสินค้าที่ปรับปรุง**: เขียนทับเมธอด `_search` ใน `product.product` เพื่อข้ามสิทธิ์การเข้าถึงโดยใช้ `sudo()` ช่วยให้สามารถดึงข้อมูลได้อย่างครบถ้วน
- **การจัดการคำสั่งซื้อขายที่ดีขึ้น**: ขยาย `sale.order` เพื่อกรองสินค้าที่สามารถขายได้และมีสต็อกในระหว่างการเลือกบรรทัดคำสั่งซื้อขาย เพื่อให้การดำเนินการขายมีความแม่นยำและมีประสิทธิภาพ

## คำอธิบายไฟล์

### 1. `models/product_product.py`

- **วัตถุประสงค์**: ปรับปรุงความสามารถในการค้นหาสินค้า
- **ฟังก์ชันหลัก**: 
  - เขียนทับเมธอด `_search` เพื่อใช้ `sudo()` ซึ่งช่วยให้การค้นหาสามารถข้ามการตรวจสอบสิทธิ์การเข้าถึงมาตรฐานได้ ทำให้การค้นหาสามารถดึงข้อมูลที่จำเป็นทั้งหมดได้โดยไม่ถูกจำกัดด้วยสิทธิ์ของผู้ใช้

### 2. `models/sale_order.py`

- **วัตถุประสงค์**: ปรับปรุงการจัดการคำสั่งซื้อขายโดยการกรองสินค้า
- **ฟังก์ชันหลัก**:
  - **_is_sale_order_line_selection**: ตรวจสอบว่าบริบทปัจจุบันคือการเลือกสินค้าสำหรับบรรทัดคำสั่งซื้อขายหรือไม่
  - **_get_product_catalog_order_data**: ใช้ `sudo()` เพื่อจัดการการเข้าถึงสินค้าและกรองสินค้าให้รวมเฉพาะสินค้าที่สามารถขายได้และมีสต็อก
  - **_get_product_catalog_order_line_info**: คล้ายกับข้างต้น มันช่วยให้มั่นใจได้ว่ามีการพิจารณาเฉพาะสินค้าที่สามารถขายได้และมีสต็อกในระหว่างการเลือกบรรทัดคำสั่งซื้อขาย

### 3. `models/product_template.py`

- **วัตถุประสงค์**: (สมมติว่ามีการปรับปรุงคล้ายกับไฟล์อื่น ๆ เนื่องจากเนื้อหาไม่สามารถมองเห็นได้ทั้งหมด)
- **ฟังก์ชันหลัก**: น่าจะขยายความสามารถของเทมเพลตสินค้าให้สอดคล้องกับการปรับปรุงในการจัดการสินค้าและคำสั่งซื้อขาย

## การติดตั้ง

1. โคลนที่เก็บลงในไดเรกทอรี addons ของ Odoo ของคุณ
2. อัปเดตรายการโมดูล Odoo โดยการรีสตาร์ทเซิร์ฟเวอร์ Odoo
3. ติดตั้งโมดูลจากอินเทอร์เฟซ Odoo Apps

## การใช้งาน

- **การค้นหาสินค้า**: ใช้ความสามารถในการค้นหาที่ปรับปรุงเพื่อดึงสินค้าที่ไม่มีข้อจำกัดในการเข้าถึง
- **การประมวลผลคำสั่งซื้อขาย**: สร้างและจัดการคำสั่งซื้อขายด้วยการเลือกสินค้าที่ปรับปรุงแล้ว เพื่อให้มั่นใจว่ามีการรวมเฉพาะสินค้าที่สามารถขายได้และมีสต็อก

## การมีส่วนร่วม

ยินดีต้อนรับการมีส่วนร่วม! โปรด fork ที่เก็บและส่ง pull request พร้อมการเปลี่ยนแปลงของคุณ

## ใบอนุญาต

โมดูลนี้ได้รับอนุญาตภายใต้ Odoo Proprietary License v1.0

---

This README provides a detailed explanation of the module's functionality in both English and Thai, suitable for developers to understand the module's purpose and usage. Adjust as needed for any additional details or specific project requirements!
