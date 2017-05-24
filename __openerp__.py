# -*- coding: utf-8 -*-
{
    'name': "OpenacademyCurriculum",

    'summary': """Curriculum info""",

    'description': """
        Open Academy module for curriculums
    """,

    'author': "Your Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','openacademy'],

    # always loaded
    'data': [
        #'security/security.xml',
        #'security/ir.model.access.csv',
        #'templates.xml',
        'views/curriculum.xml',
        #'views/session_workflow.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    #    'demo.xml',
    ],
    'installable': True,
    'active': False,
}
