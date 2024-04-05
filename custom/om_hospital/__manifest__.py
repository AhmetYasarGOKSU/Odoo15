# -*- coding: utf-8 -*-
{
    'name': 'Hospital Management',
    'summary': 'Hospital Management Software',
    'description': '''Hospital Management Software
    ''',
    'sequence': -100,
    'version': '1.0',
    'category': 'Productivity',
    'website': 'https://www.odoomates.tech',
    'depends': [
                'sale',
                'mail'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/patient_view.xml',
        'views/kids_view.xml',
        'views/sale.xml'
    ],
    'demo':[],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}