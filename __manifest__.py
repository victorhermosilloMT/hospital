# -*- coding: utf-8 -*-
{
    'name': "Hospital",

    'summary': """Manage hospital information""",

    'description': """Manage the files and patients of an hospital""",

    'author': "Victor Hermosillo - MTnet",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '12.0.0.1.2',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/employee.xml',
        'views/patient.xml',
        'views/file.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'sequence': 1,
}