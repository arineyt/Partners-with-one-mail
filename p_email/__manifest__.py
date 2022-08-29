{
    'name': "p_email",

    'summary': """
        Partners with one e-mail""",

    'author': "Dmytro Stopchak",
    'images': ['static/description/banner.png',
               'static/description/icon.png'],

    'category': 'Uncategorized',
    'version': '15.0.1.0.0',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
    ],
}
