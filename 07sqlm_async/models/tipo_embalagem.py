from typing import Optional
from sqlmodel import Field, SQLModel
from datetime import datetime



class TipoEmbalagem(SQLModel, table=True):
    __tablename__: str = 'tipos_embalagem'

    id: Optional[int] = Field(default=None, primary_key=True)
    data_criacao: datetime = Field(default=datetime.now(), index=True)
    
    nome: str = Field(max_length=45, unique=True)

    def __repr__(self) -> str:
        return f'<Tipo Embalagem: {self.nome}>'