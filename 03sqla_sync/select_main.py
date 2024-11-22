from typing import List
from sqlalchemy import func
from conf.helpers import formata_data
from conf.db_session import create_session
# select simples
from models.aditivo_nutritivo import AditivoNutritivo
from models.sabor import Sabor
from models.revendedor import Revendedor
# select compostos/complexos
from models.picole import Picole


## Select simples -> SELECT * FROM aditivos_nutritivos
def select_todos_aditivos_nutritivos() -> None:
    with create_session() as session:
        # forma 1
        #aditivos_nutritivos: List[AditivoNutritivo] = session.query(AditivoNutritivo)

        #forma 2
        aditivos_nutritivos: List[AditivoNutritivo] = session.query(AditivoNutritivo).all()

        for an in aditivos_nutritivos:
            print(f'ID: {an.id}')
            print(f'Data: {formata_data(an.data_criacao)}')
            print(f'Nome: {an.nome}')
            print(f'Fórmula Química: {an.formula_quimica}')


def select_filtro_sabor(id_sabor: int) -> None:
    with create_session() as session:
        # forma 1 -> Retona none caso nao encontre
        # sabor: Sabor = session.query(Sabor).filter(Sabor.id == id_sabor).first()

        # forma 2 -> Retona none caso nao encontre(Recomendado)
        # sabor: Sabor = session.query(Sabor).filter(Sabor.id == id_sabor).one_or_none()

        # forma 3 -> Retona exec.NoresultFound caso nao encontr
        # sabor: Sabor = session.query(Sabor).filter(Sabor.id == id_sabor).one()

        # forma 4 -> Usando where (one, one_or_none, first)
        sabor: Sabor = session.query(Sabor).where(Sabor.id == id_sabor).one_or_none()

        print(f"ID: {sabor.id}")
        print(f"Data: {formata_data(sabor.data_criacao)}")
        print(f"Nome: {sabor.nome}")


def select_complexo_picole() -> None:
    with create_session() as session:
        picoles: List[Picole] = session.query(Picole).all()

        for picole in picoles:
            print(f'ID: {picole.id}')
            print(f'Data: {formata_data(picole.data_criacao)}')
            print(f'Preço: {picole.preco}')

            print(f'ID Sabor: {picole.id_sabor}')
            print(f'Sabor: {picole.sabor.nome}')

            print(f'ID Embalagem: {picole.id_tipo_embalagem}')
            print(f'Embalagem: {picole.tipo_embalagem.nome}')

            print(f'ID Picolé: {picole.id_tipo_picole}')
            print(f'Tipo Picolé: {picole.tipo_picole.nome}')

            print(f'Ingredientes: {picole.ingredientes}')
            print(f'Aditivos Nutritivos: {picole.aditivos_nutritivos}')
            print(f'Conservantes: {picole.conservantes}')


def select_order_by_sabor() -> None:
    with create_session() as session:
        sabores: List[Sabor] = session.query(Sabor).order_by(Sabor.data_criacao.desc()).all()

        for sabor in sabores:
            print(f"ID: {sabor.id}")
            print(f"Nome: {sabor.nome}")


if __name__ == '__main__':
    # select_todos_aditivos_nutritivos()
    # select_filtro_sabor(21)
    # select_complexo_picole()
    select_order_by_sabor()