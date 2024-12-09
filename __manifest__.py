# Creado por Andres Sanchez - Fecha: 2024-11-07
{
    'name': "Gestión de Inspecciones Obligatorias",
    'version': '3.0',
    'summary': """
        Gestión centralizada de inspecciones obligatorias en instalaciones hoteleras.
        Cronología:
        - Versión 2.6: Añadido soporte para vista Kanban y resaltado de inspecciones próximas en rojo.
        - Versión 2.5: Inclusión de Entidades Inspectoras con campos de contacto.
        - Versión 2.4: Introducción del modelo básico de inspecciones con periodicidad y adjuntos.
        - Versión 2.7: Se añade el módulo de Tipos de Inspección con estados editables.
    """,
    'author': "Andres Sanchez",
    'website': "https://boitaullresort.com",
    'license': 'LGPL-3',
    'category': 'Maintenance',
    'depends': ['maintenance', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/inspection_views.xml',
        'views/inspection_action_views.xml',
        'views/inspection_menu_views.xml',
        'views/inspection_calendar_views.xml',
        'views/inspection_entity_views.xml',
        'views/inspection_type_views.xml',
        'data/inspection_data.xml',
    ],
    
    'installable': True,
    'application': True,
    'auto_install': False,
}


