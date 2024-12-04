from typing import Optional
from sqlmodel import Field, SQLModel
from datetime import datetime



class Sabor(SQLModel, table=True):
    __tablename__: str = 'sabores'

    id: Optional[int] = Field(primary_key=True, autoincrement=True)
    data_criacao: datetime = Field(default=datetime.now, index=True)
    
    nome: str = Field(max_length=45, unique=True)

    def __repr__(self) -> str:
        return f'<Sabor: {self.nome}>'