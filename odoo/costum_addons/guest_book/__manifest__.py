{
    "name" : "Guest Book",
    "version" : "1.0",
    "author" : "Habib",
    "category" : "tools",
    "installable" : True,
    "application" : True,
    'depends': ['base'],
    "data" : [
        "views/guest_book_views.xml", "security/ir.model.access.csv", "security/security.xml"
    ]
}