from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime
from typing import List, Optional
from pydantic import condecimal
#models
from models.sabor import Sabor
from models.tipo_embalagem import TipoEmbalagem
from models.tipo_picole import TipoPicole
from models.ingrediente import Ingrediente
from models.conservante import Conservante
from models.aditivo_nutritivo import AditivoNutritivo

#Many to many picole/ingrediente
class IngredientesPicole(SQLModel, table=True): 
    id: Optional[int] = Field(default=None, primary_key=True)
    id_picole: Optional[int] = Field(default=None, foreign_key ="picoles.id")
    id_ingrediente: Optional[int] = Field(default=True, foreign_key="ingredientes.id")


#Many to many picole/conservante
class ConservantesPicole(SQLModel, table=True): 
    id: Optional[int] = Field(default=None, primary_key=True)
    id_picole: Optional[int] = Field(default=None, foreign_key = "picoles.id")
    id_conservante: Optional[int] = Field(default=None, foreign_key="conservantes.id")



#Many to many picole/aditivo_nutritivo
class AditivosNutritivosPicole(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    id_picole: Optional[int] = Field(default=None, foreign_key = "picoles.id")
    id_aditivo_nutritivo: Optional[int] = Field(default=None, foreign_key="aditivos_nutritivos.id")



class Picole(SQLModel, table=True):
    __tablename__: str = 'picoles'

    id: Optional[int] = Field(default=None, primary_key=True)
    data_criacao: datetime = Field(default=datetime.now, index=True)
    
    preco: condecimal(max_digits=5, decimal_places=2) = Field(default=0) 

    id_sabor: int = Field(foreign_key='sabores.id')
    sabor: Sabor = Relationship(sa_relationship_kwargs={"lazy": "joined"})

    id_tipo_embalagem: int = Field(foreign_key='tipos_embalagem.id')
    tipo_embalagem: TipoEmbalagem = Relationship(sa_relationship_kwargs={"lazy": "joined"})

    id_tipo_picole: int = Field(foreign_key='tipos_picole.id')
    tipo_picole: TipoPicole = Relationship(sa_relationship_kwargs={"lazy": "joined"})

    ingredientes: List[Ingrediente] = Relationship(link_model=IngredientesPicole, sa_relationship_kwargs={"lazy": "joined"})
    conservantes: Optional[List[Conservante]] = Relationship(link_model=ConservantesPicole, sa_relationship_kwargs={"lazy": "joined"})
    aditivos_nutritivos: Optional[List[AditivoNutritivo]] = Relationship(link_model=AditivosNutritivosPicole,sa_relationship_kwargs={"lazy": "joined"})
    
    def __repr__(self) -> str:
        return f'<Picole: {self.tipo_picole.nome} com sabor {self.sabor.nome} e preço {self.preco}>'