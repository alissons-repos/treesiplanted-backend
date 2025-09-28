# Configurações da aplicação e do banco de dados


class BaseConfig:
    """Configuração base da aplicação."""

    API_TITLE = "Trees API"
    API_VERSION = "1.0.0"
    OPENAPI_VERSION = "3.0.3"
    OPENAPI_URL_PREFIX = "/"
    OPENAPI_JSON_PATH = "openapi.json"
    OPENAPI_SWAGGER_UI_PATH = "/swagger-ui"
    OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    SQLALCHEMY_DATABASE_URI = "sqlite:///treesiplanted.sqlite3"
    SQLALCHEMY_ENGINE_OPTIONS = {"future": True}
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_SORT_KEYS = False
    JSONIFY_PRETTYPRINT_REGULAR = True
    PROPAGATE_EXCEPTIONS = True

    API_SPEC_OPTIONS = {
        "info": {
            "description": "API para registrar e gerenciar árvores plantadas.",
        },
        "tags": [
            {"name": "trees", "description": "Operações para manipulação de árvores."}
        ],
    }

    OPENAPI_SWAGGER_UI_CONFIG = {
        "docExpansion": "list",
        "displayRequestDuration": True,
        "tryItOutEnabled": True,
        "syntaxHighlight": True,
    }
