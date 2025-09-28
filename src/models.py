# Modelo SQLAlchemy de uma árvore (Tree)

from datetime import date
from src.db import db


class Tree(db.Model):
    """Mdelos do banco de dados que representa uma árvore plantada."""
    __tablename__ = "trees"

    id = db.Column(db.Integer, primary_key=True)
    custom_name = db.Column(db.String(128), nullable=False, index=True)
    species = db.Column(db.String(128), nullable=True, index=True)
    location = db.Column(db.String(256), nullable=False)
    planting_date = db.Column(db.Date, nullable=False, index=True)

    def __repr__(self):
        """Retorna uma string representando amigavelmente uma árvore."""
        return f"<Tree id={self.id} custom_name={self.custom_name!r} species={self.species!r}>"
