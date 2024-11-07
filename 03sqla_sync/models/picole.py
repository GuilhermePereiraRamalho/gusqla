#models
import sqlalchemy as sa
import sqlalchemy.orm as orm

from datetime import datetime
from typing import List, Optional

#models
from models.model_base import ModelBase
from models.sabor import Sabor
from models.tipo_embalagem import TipoEmbalagem
from models.tipo_picole import TipoPicole
from models.ingrediente import Ingrediente
from models.conservante import Conservante
from models.aditivo_nutritivo import AditivoNutritivo

#Many to many picole/ingrediente
ingredientes_picole = sa.Table(
    "ingredientes_picole",
    ModelBase.metadata,
    sa.column('id_picole', sa.Integer, sa.ForeignKey("picoles.id")),
    sa.column('id_ingrediente', sa.Integer, sa.ForeignKey("ingredientes.id"))
)

#Many to many picole/conservante
conservantes_picole = sa.Table(
    "conservantes_picole",
    ModelBase.metadata,
    sa.column('id_picole', sa.Integer, sa.ForeignKey("picoles.id")),
    sa.column('id_conservante', sa.Integer, sa.ForeignKey("conservantes.id"))
)

#Many to many picole/aditivo_nutritivo
aditivos_nutritivos_picole = sa.Table(
    "aditivos_nutritivos_picole",
    ModelBase.metadata,
    sa.column('id_picole', sa.Integer, sa.ForeignKey("picoles.id")),
    sa.column('id_aditivo_nutritivo', sa.Integer, sa.ForeignKey("aditivos_nutritivos.id"))
)


class Picole(ModelBase):
    __tablename__: str = 'picoles'

    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    
    preco: float = sa.Column(sa.DECIMAL(8,2), nullable=False)

    id_sabor: int = sa.Column(sa.Integer, sa.ForeignKey('sabores.id'))
    sabor: Sabor = orm.relationship('Sabor', lazy='joined')

    id_tipo_embalagem: int = sa.Column(sa.Integer, sa.ForeignKey('tipos_embalagem.id'))
    tipo_embalagem: TipoEmbalagem = orm.relationship('TipoEmbalagem', lazy='joined')

    id_tipo_picole: int = sa.Column(sa.Integer, sa.ForeignKey('tipos_picole.id'))
    tipo_picole: TipoPicole = orm.relationship('TipoPicole', lazy='joined')

    ingredientes: List[Ingrediente] = orm.relationship('Ingrediente', secondary=ingredientes_picole, backref='ingrediente', lazy='joined')
    conservantes: Optional[List[Conservante]] = orm.relationship('Conservante', secondary=conservantes_picole, backref='conservante', lazy='joined')
    aditivos_nutritivos: Optional[List[AditivoNutritivo]] = orm.relationship('AditivoNutritivo', secondary=aditivos_nutritivos_picole, backref='aditivo_nutritivo', lazy='joined')
    
    def __repr__(self) -> str:
        return f'<Picole: {self.tipo_picole.nome} com sabor {self.sabor.nome} e preço {self.preco}>'