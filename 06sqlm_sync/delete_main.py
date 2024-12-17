from typing import Optional
from conf.db_session import create_session
from models.revendedor import Revendedor
from models.picole import Picole



def deletar_picole(id_picole: int) -> None:
    with create_session() as session:
        picole: Optional[Picole] = session.get(Picole, id_picole)

        if picole:
            session.delete(picole)
            session.commit()
        else:
            print(f"Picolé de id {id_picole} não encontrado!")


def select_filtro_revendedor(id_revendedor: int) -> None:
    with create_session() as session:
        revendedor: Optional[Revendedor] = session.get(Revendedor, id_revendedor)

        if revendedor:
            print(f'ID: {revendedor.id}')
            print(f'Razão Social: {revendedor.razao_social}')
        else:
            print(f'Não encontrei nenhum revendedor com id {id_revendedor}')


def deletar_revendedor(id_revendedor: int) -> None:
    with create_session() as session:
        revendedor: Optional[Revendedor] = session.get(Revendedor, id_revendedor)

        if revendedor:
            session.delete(revendedor)
            session.commit()
        else:
            print(f'Não encontrei nenhum revendedor com id {id_revendedor}')


if __name__ == '__main__':
    # from update_main import select_filtro_picole

    # id_picole = 21

    # # Antes
    # select_filtro_picole(id_picole=id_picole)    

    # # Deletar
    # deletar_picole(id_picole=id_picole)

    # # Depois
    # select_filtro_picole(id_picole=id_picole)

    # # Nao vinculado
    # id_revendedor_nv = 3

    # Vinculado
    id_revendedor_v = 5

    # Antes
    select_filtro_revendedor(id_revendedor=id_revendedor_v)

    # Deletar
    deletar_revendedor(id_revendedor=id_revendedor_v)

    # Depois
    select_filtro_revendedor(id_revendedor=id_revendedor_v)