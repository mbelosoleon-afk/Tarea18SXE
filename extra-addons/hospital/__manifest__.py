# -*- coding: utf-8 -*-
{
    'name': "hospital",

    'summary': "Módulo que permite gestionar pacientes y médicos de un hospital",

    'description': """
HOSPITAL DONDE LOS MÉDICOS NO SON MUY BUENOS ASÍ QUE TENGO QUE HACERLES YO EL TRABAJO CON LOS 
DIAGNÓSTICOS DE LOS PACIENTES. LA SANIDAD EMPEORA CADA VEZ MÁS.
    """,

    'author': "Daniel Castelao",
    'website': "https://www.danielcastelao.org",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
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

