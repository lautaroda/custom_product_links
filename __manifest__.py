# __manifest__.py
{
    'name': 'Product Move Document Links',
    'version': '1.0',
    'category': 'Inventory',
    'summary': 'Adds direct links to related documents in product moves',
    'description': """
    This module allows users to click on links within product move records to directly access related documents such as purchase orders and sales orders.
    """,
    'author': 'Lautaro De Angelis',
    'website': ' ',
    'depends': ['stock'],
    'data': [
        'views/product_move_view.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
