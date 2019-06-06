#Author: Thiep Wong
#Created: 18.5/2019
#Reponsive interface for the mobile web app

{
    "name": "SmartERP Web resonsive",
    "summary": "Responsive web client for SmartERP",
    "version": "12.0.1.1.0",
    "category": "Website",
    "website": "http://www.smartlifevn.com.vn",
    "author": "Thiep Wong",
    "license": "LGPL-3",
    "installable": True,
    "depends": [
        'web',
        'mail',
    ],
    "data": [
        'views/assets.xml',
        'views/res_users.xml',
        'views/web.xml',
    ],
    'qweb': [
        'static/src/xml/apps.xml',
        'static/src/xml/form_view.xml',
        'static/src/xml/navbar.xml',
    ],
}
