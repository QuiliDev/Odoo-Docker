{
    'name': 'DidaktikApp',
    'version': '1.0',
    'depends': ['base', 'contacts', 'hr'],
    'data': [
        'data/employee_category.xml',
        'views/res_partner_view.xml',
        'security/ir.model.access.csv',
        'views/app_views.xml',
        'security/record_rules.xml',
        'views/horas_views.xml'
    ],
    'application': True, 
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3', 
}