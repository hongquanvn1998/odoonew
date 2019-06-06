# -*- coding: utf-8 -*-
{
    'name': "admin",

    'summary': """
        Module này dùng để khởi tạo db và tạo đường dẫn ban đầu
        """,

    'description': """
        Module này dùng để khởi tạo db và tạo đường dẫn ban đầu
    """,

    'author': "Smartlife Inc",
    'website': "http://www.smartlifevn.com.vn",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Hidden',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],
    'auto_install': True,
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'bootstrap': True,
}