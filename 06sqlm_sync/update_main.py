from conf.db_session import create_session
from models.sabor import Sabor
from models.picole import Picole
from sqlmodel import select


def select_filtro_picole(id_picole: int) -> None:
    with create_session() as session:
        picole: Picole = session.get(Picole, id_picole)

        if picole:
            print(f"ID: {picole.id}")
            print(f"Preço: {picole.preco}")
            print(f"Sabor: {picole.sabor.nome}")
        else:
            print('Não existe picole com o ID informado')


def atualizar_sabor(id_sabor: int, novo_nome:str) -> None:
    with create_session() as session:
        sabor: Sabor = session.get(Sabor, id_sabor)

        if sabor:
            sabor.nome = novo_nome
            session.commit()
        else:
            print(f'Não existe um sabor com ID: {id_sabor}')


def atualizar_picole(id_picole: int, novo_preco: float, novo_sabor: int = None) -> None:
    with create_session() as session:
        picole: Picole = session.get(Picole, id_picole)

        if picole:
            picole.preco = novo_preco
            if novo_sabor:
                picole.id_sabor=novo_sabor
            session.commit()
        else:
            print(f'Não existe picolé com o ID: {id_picole}')


if __name__ == '__main__':
    # from select_main import select_filtro_sabor
    # id_sabor = 42
    # select_filtro_sabor(id_sabor)

    # atualizar_sabor(id_sabor=id_sabor, novo_nome="Banana")

    # select_filtro_sabor(id_sabor)

    id_picole = 21
    novo_preco = 6.66
    id_novo_sabor = 42

    select_filtro_picole(id_picole=id_picole)
    atualizar_picole(id_picole=id_picole, novo_preco=novo_preco, novo_sabor=id_novo_sabor)
    select_filtro_picole(id_picole=id_picole)
