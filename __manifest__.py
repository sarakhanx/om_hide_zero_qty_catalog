{
    'name': 'Hide Zero Quantity Products',
    'version': '17.0.1.0.0',
    'category': 'Sales',
    'summary': 'ซ่อนสินค้าจาก catalog หากไม่มีสินค้าในคลัง',
    'description': """
        ซ่อนสินค้าที่ไม่มีสินค้าในคลัง
        - การไม่อนุญาติให้ขายสินค้าที่ขาดสินค้า
        - การซ่อนสินค้าที่มีคุณสมบัติของสินค้าที่ขาดสินค้า
        Features:
        - Hides products with zero quantity from catalog views
        - Prevents sales users from selling out-of-stock products
    """,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'depends': ['sale_management', 'stock'],
    'data': [
        'security/product_security.xml',
        'security/ir.model.access.csv',
        'views/search_views.xml',
        'views/action_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
} 