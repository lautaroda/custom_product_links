{
    'name': 'Product Move Links',
    'version': '1.0',
    'summary': 'Agrega enlaces a documentos relacionados en la vista tipo árbol de movimientos de producto',
    'category': 'Inventory',
    'author': 'Lautaro De Angelis',
    'website': 'https://www.tuempresa.com',
    'depends': ['stock', 'purchase', 'sale'],
    'data': [
        'views/product_move_view.xml',
    ],
    'installable': True,
    'application': False,
}
