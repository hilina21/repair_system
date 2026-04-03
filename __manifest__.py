{
    "name": "Gadget Repair",
    "version": "17.0.1.0.0",
    "category": "Tools",
    "depends": ["base", "web"],
    "data": [
        "security/ir.model.access.csv",
        "views/gadjet.xml",
        "views/menu.xml",
        
        
    ],
    'assets': {
    'web.assets_backend': [
        'repair_system/static/src/js/dashboard.js',
        'repair_system/static/src/xml/dashboard_template.xml',
    ],

    },
    "installable": True,
    "application": True,
}