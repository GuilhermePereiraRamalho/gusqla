from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime
from pydantic import condecimal
from models.revendedor import Revendedor
from models.lote import Lote

class LotesNotaFiscal (SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, autoincrement=True)
    id_nota_fical: Optional[int] = Field(default=None, foreign_key="notas_fiscais.id"),
    id_lote: Optional[int] = Field(default=None, foreign_key="lotes.id")


class NotaFiscal(SQLModel, table=True):
    __tablename__: str = 'notas_fiscais'

    id: Optional[int] = Field(primary_key=True, autoincrement=True)
    data_criacao: datetime = Field(default=datetime.now, index=True)
    
    valor: condecimal(max_digits=5, decimal_places=2) = Field(default=0)
    numero_serie: str = Field(max_length=45, unique=True)
    descricao: str = Field(max_length=200, nullable=False)

    id_revendedor: Optional[int] = Field(foreign_key='revendedores.id', ondelete="CASCADE")
    revendedor: Revendedor = Relationship(lazy="joined", cascade="delete")

    lotes: List[Lote] = Relationship(link_model=LotesNotaFiscal, back_populates='lote', lazy='dynamic')

    def __repr__(self) -> str:
        return f'<Nota Fiscal: {self.numero_serie}>'