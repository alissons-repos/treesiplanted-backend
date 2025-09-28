# Schemas marshmallow para validação + documentação OpenAPI

from marshmallow import Schema, fields, validate, EXCLUDE

# Validação simples de string não vazia
_nonempty = validate.Length(min=1, error="O campo não pode ser vazio.")


class BaseSchema(Schema):
    """Schema base para comportamentos comuns."""

    class Meta:
        ordered = True
        unknown = EXCLUDE  # Campos extras são ignorados


class TreeBaseSchema(BaseSchema):
    """Campos comuns de uma árvore."""

    custom_name = fields.String(
        required=True,
        validate=_nonempty,
        metadata={
            "description": "Nome amigável dado à árvore.",
            "example": "Carvalho Imperial",
        },
    )
    species = fields.String(
        required=False,
        allow_none=True,
        metadata={
            "description": "Espécie botânica (opcional).",
            "example": "Quercus robur",
        },
    )
    location = fields.String(
        required=True,
        validate=_nonempty,
        metadata={
            "description": "Localização textual da árvore.",
            "example": "Parque da Cidade, Brasília - DF",
        },
    )
    planting_date = fields.Date(
        required=True,
        metadata={
            "description": "Data de plantio no formato ISO (YYYY-MM-DD).",
            "example": "2024-03-15",  # formato ISO para casar com a validação do marshmallow
        },
    )


class TreeResponseSchema(TreeBaseSchema):
    """Resposta da árvore com identificador."""

    id = fields.Integer(
        required=True,
        dump_only=True,
        metadata={"description": "Identificador interno da árvore.", "example": 1},
    )


class TreeCreateSchema(TreeBaseSchema):
    """Payload para criar uma nova árvore."""

    id = fields.Integer(dump_only=True)


class TreeUpdateSchema(TreeBaseSchema):
    """Payload para atualizar parcialmente uma árvore existente (qualquer campo)."""

    custom_name = fields.String(
        metadata={
            "description": "Nome amigável dado à árvore.",
            "example": "Ipê Amarelo",
        },
    )
    species = fields.String(
        metadata={
            "description": "Espécie botânica (opcional).",
            "example": "Handroanthus albus",
        },
    )
    location = fields.String(
        metadata={
            "description": "Localização textual da árvore.",
            "example": "Praça Central",
        },
    )
    planting_date = fields.Date(
        metadata={
            "description": "Data de plantio no formato ISO (YYYY-MM-DD).",
            "example": "2023-09-01",
        },
    )
