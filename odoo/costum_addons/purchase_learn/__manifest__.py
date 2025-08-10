{
    "name" : "Purchase Custom",
    "author" : "Habib",
    "category" : "tools",
    "installable" : True,
    "application" : True,
    "depends" : ["base", "web", "product"],
    "data": [
        "security/ir.model.access.csv",
        "views/purchase_learn_view.xml",
        "views/purchase_learn_action.xml",
        "views/purchase_learn_menuitem.xml",
        "views/purchase_learn_sequence.xml",
        "views/purchase_learn_cron.xml"
    ],
    "license" : "LGPL-3"
}