from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime

from models.tipo_picole import TipoPicole


class Lote(SQLModel, table=True):
    __tablename__: str = 'lotes'

    id: Optional[int] = Field(default=None, primary_key=True)
    data_criacao: datetime = Field(default=datetime.now(), index=True)

    id_tipo_picole: Optional[int] = Field(default=None, foreign_key='tipos_picole.id')
    tipo_picole: TipoPicole = Relationship(sa_relationship_kwargs={"lazy": "joined"})

    quantidade: int = Field()

    def __repr__(self) -> str:
        return f'<Lote: {self.id}>'