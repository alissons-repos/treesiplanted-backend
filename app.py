# Arquivo principal da aplicação Flask

from flask import Flask
from flask_smorest import Api
from flask_cors import CORS
from config import BaseConfig
from src.db import db
from src.routes.trees import blp as TreesBlueprint


def create_app(config_object=BaseConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)

    # Habilita CORS para toda a API (inclui /openapi.json e /swagger-ui)
    CORS(app)

    # Inicializa extensões
    db.init_app(app)

    # Registra API (OpenAPI 3 + Swagger UI)
    api = Api(app)
    api.register_blueprint(TreesBlueprint)

    # Cria tabelas, caso não existam
    @app.before_request
    def _create_tables():
        db.create_all()

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
