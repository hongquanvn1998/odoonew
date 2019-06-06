# -*- coding: utf-8 -*-
# Author: Thiep Wong
# Created: 18.5/2019

{
    "name": "Home Dashboard",
    "summary": "Home dashboard for SmartERP",
    "version": "12.0.0.1",
    "category": "Theme/Backend",
    "website": "http://www.smartlifevn.com.vn",
	"description": """
		 This is home dashboard for smart ERP -- A SLM product
    """,
	'images':[
        'images/screen.png'
	],
    "author": "Thiep Wong",
    "license": "LGPL-3",
    "installable": True,
    "depends": [
        'web',
        'home_web_responsive',

    ],
    "data": [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/assets.xml',
		'views/res_company_view.xml',
		'views/users.xml',
        'views/sidebar.xml',
		'views/web.xml',
    ],
    'auto_install': True,
    'application': True,

}



# # -*- coding: utf-8 -*-
# {
#     'name': "Trang chủ ứng dụng",

#     'summary': """
#        Các ứng dụng đã cài đặt sẽ được thể hiện tại đây! Click chọn ứng dụng để chuyển sang
#        """,

#     'description': """
#          Đây là module cho trang chủ của hệ thống ERP
#     """,

#     'author': "@Thiep Wong",
#     'website': "http://www.smartlifevn.com",

#     # Categories can be used to filter modules in modules listing
#     # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
#     # for the full list
#     'category': 'Uncategorized',
#     'version': '0.1',

#     # any module necessary for this one to work correctly
#     'depends': ['base'],

#     # always loaded
#     'data': [
#         'security/ir.model.access.csv',
#         'views/views.xml',
#         'views/templates.xml',
#     ],
#     # only loaded in demonstration mode
#     'demo': [
#         'demo/demo.xml',
#     ], 
#     'installable': True,
#     'application': True,
#     'auto_install': True,
#     'images': ['static/description/banner.gif'],
#     'qweb': [],
# }