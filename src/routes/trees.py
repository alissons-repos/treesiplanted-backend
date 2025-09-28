# Blueprint de rotas CRUD para árvores

from flask import abort
from flask.views import MethodView
from flask_smorest import Blueprint
from sqlalchemy.exc import IntegrityError
from src.db import db
from src.models import Tree
from src.schemas import TreeCreateSchema, TreeResponseSchema, TreeUpdateSchema

blp = Blueprint("trees", __name__, description="Operações para manipulação de árvores.")


@blp.route("/trees")
class TreesCollection(MethodView):
    """Coleção de árvores."""

    @blp.response(200, TreeResponseSchema(many=True))
    def get(self):
        """Lista todas as árvores.

        Retorna:
            list[Tree] - A lista de todas as suas árvores.
        """
        # Retorna todas as árvores do bando de dados
        trees = Tree.query.order_by(Tree.id.asc()).all()
        return trees

    @blp.arguments(TreeCreateSchema)
    @blp.response(201, TreeResponseSchema)
    @blp.alt_response(422, description="Payload inválido ou erro de integridade")
    def post(self, payload):
        """Cria uma nova árvore.

        Argumentos:
            payload (dict) - Campos válidos para a nova árvore.

        Retorna:
            Tree - A árvore que você acabou de criar.
        """
        # Cria e persiste uma nova árvore no banco de dados
        tree = Tree(**payload)
        db.session.add(tree)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            abort(
                400,
                description="Não foi possível criar a árvore devido a um erro de integridade.",
            )
        return tree


@blp.route("/trees/<int:tree_id>")
class TreeItem(MethodView):
    """Recurso individual de árvore."""

    @blp.arguments(TreeUpdateSchema)
    @blp.response(200, TreeResponseSchema)
    @blp.alt_response(422, description="Payload inválido ou erro de integridade")
    @blp.alt_response(404, description="Árvore não encontrada")
    def put(self, payload, tree_id: int):
        """Atualiza uma árvore a partir de seu identificador.

        Argumentos:
            payload (dict) - Campos a serem atualizados.
            tree_id (int) - O identificador da árvore.

        Retorna:
            Tree - A árvore atualizada.
        """
        # Atualiza somente os campos enviados
        tree = Tree.query.get_or_404(tree_id, description="Árvore não encontrada.")

        for key, value in payload.items():
            setattr(tree, key, value)

        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            abort(
                400,
                description="Não foi possível atualizar a árvore devido a erro de integridade.",
            )
        return tree

    @blp.response(204)
    @blp.alt_response(404, description="Árvore não encontrada")
    def delete(self, tree_id: int):
        """Deleta uma árvore a partir de seu identificador.

        Argumentos:
            tree_id (int) - O identificador da árvore.

        Retorna:
            None - Uma string vazia.
        """
        # Exclui a árvore, caso ela exista no banco de dados
        tree = Tree.query.get_or_404(tree_id, description="Árvore não encontrada.")
        db.session.delete(tree)
        db.session.commit()
        return ""
