{
    'name': 'Vendor Bill Payment Number',
    'summary': "Show reconciled payment numbers on Vendor Bills",
    'version': '15.0.1.1.0',
    'description': """
        This module adds a computed field to Vendor Bills (account.move)
        that displays the Payment Number(s) reconciled with the bill.
        Useful for accounting visibility and reporting.
    """,
    'author': 'Nattanai Vinyangkoon, The Auto-Info Co., Ltd.',
    'company': 'The Auto-Info Co., Ltd.',
    'website': '',
    'category': 'Accounting',
    'depends': ['account'],
    'license': 'LGPL-3',
    'data': [
        'views/account_move_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
