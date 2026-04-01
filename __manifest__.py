{
    "name": "Gadjet",   
    "category": "G2P",
    "version": "17.0.0.0.0",
    "sequence": 1,
    "license": "LGPL-3",
    "depends": [],
    "data": [
       "security/ir.model.access.csv",
       "views/gadjet.xml",
    #    "views/dashboard.xml", 
       "views/menu.xml",
       ],

    "installable": True,
    'application': True,
    "depends": ["base", "mail"],
    
    "assets": {
        "web.assets_backend": [
            "repair_system/static/src/js/dashboard.js",
            "repair_system/views/dashboard_template.xml",
        ],
    },
}


