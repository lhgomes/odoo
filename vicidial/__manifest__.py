# -*- coding: utf-8 -*-
{
    'name': "Vicidial",

    'summary': """
        Integration with Vicidial dialer platform""",

    'description': """
        This module was created to integrate our Vicidial Softphone with Odoo
        and provide an easy way to make and receive calls from an Vicidial Server
    """,

    'author': "Integradial Solutions",
    'website': "http://www.integradial.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

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
}
