from guillotina import configure

app_settings = {
    "load_utilities": {
        "catalog": {
            "provides": "guillotina_pgcatalog.utility.ICatalogUtility",  # noqa
            "factory": "guillotina_pgcatalog.utility.PGSearchUtility",
            "settings": {}
        }
    },
}


def includeme(root):
    configure.scan('guillotina_pgcatalog.api')
    configure.scan('guillotina_pgcatalog.utility')
