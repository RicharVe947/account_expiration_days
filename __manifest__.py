# Copyright 2022 Munin
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    'name': 'Account Expiration Days',
    'description': """
        Adds Days to Expire in account move""",
    'version': '15.0.1.0.1',
    'license': 'AGPL-3',
    'author': 'Munin',
    'depends': [
        'base',
        'account_reports'
    ],
    'data': [
        'security/account_account_security.xml',
        'data/account_move.xml',
        'views/account_move.xml',
        'views/account_payment_term_view.xml',
    ],
    'demo': [
    ],
    'pre_init_hook': '_pre_init_hook_set_new_expiration_date',
}
