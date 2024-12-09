# Fecha: 2024-12-04
# Nombre del archivo: __manifest__.py
# Versión del archivo: V3.2

{
    'name': 'Gestión de Inspecciones Obligatorias',
    'version': '16.0.3.2',
    'summary': 'Gestión centralizada de inspecciones obligatorias en instalaciones hoteleras.',
    'description': """
        Este módulo permite gestionar inspecciones obligatorias, incluyendo tipos, responsables y resultados.
    """,
    'category': 'Operations',
    'author': 'Andrés Sánchez -- Boi Taull Resort',
    'license': 'LGPL-3',
    'depends': ['base', 'maintenance'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/inspeccion_views.xml',
        'views/entidad_inspectora_views.xml',
        'views/tipo_inspeccion_views.xml',
        'views/menus_views.xml',
        'data/entidad_inspectora_data.xml',
        'data/tipo_inspeccion_data.xml',
        'data/inspeccion_data.xml',
    ],
    'assets': {
        'web.assets_backend': [
            '/BTR_inspeccion_Rpo7/static/description/inspeccion.png',
        ],
    },
    'images': ['/BTR_inspeccion_Rpo7/static/description/inspeccion.png'],
    'application': True,
    'installable': True,
}
