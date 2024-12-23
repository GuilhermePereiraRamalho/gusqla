from typing import Optional
from conf.db_session import create_session
from models.revendedor import Revendedor
from models.picole import Picole
import asyncio


async def deletar_picole(id_picole: int) -> None:
    async with create_session() as session:
        picole: Optional[Picole] = await session.get(Picole, id_picole)

        if picole:
            await session.delete(picole)
            await session.commit()
        else:
            print(f"Picolé de id {id_picole} não encontrado!")


async def select_filtro_revendedor(id_revendedor: int) -> None:
    async with create_session() as session:
        revendedor: Optional[Revendedor] = await session.get(Revendedor, id_revendedor)

        if revendedor:
            print(f'ID: {revendedor.id}')
            print(f'Razão Social: {revendedor.razao_social}')
        else:
            print(f'Não encontrei nenhum revendedor com id {id_revendedor}')


async def deletar_revendedor(id_revendedor: int) -> None:
    async with create_session() as session:
        revendedor: Optional[Revendedor] = await session.get(Revendedor, id_revendedor)

        if revendedor:
            await session.delete(revendedor)
            await session.commit()
        else:
            print(f'Não encontrei nenhum revendedor com id {id_revendedor}')



async def deleta_picole():
    from update_main import select_filtro_picole

    id_picole = 21

    # Antes
    await select_filtro_picole(id_picole=id_picole)    

    # Deletar
    await deletar_picole(id_picole=id_picole)

    # Depois
    await select_filtro_picole(id_picole=id_picole)


async def deleta_revendedor():   
    # # Nao vinculado
    # id_revendedor_nv = 1

    # Vinculado
    id_revendedor_v = 2

    # Antes
    await select_filtro_revendedor(id_revendedor=id_revendedor_v)

    # Deletar
    await deletar_revendedor(id_revendedor=id_revendedor_v)

    # Depois
    await select_filtro_revendedor(id_revendedor=id_revendedor_v)


if __name__ == '__main__':
    # asyncio.run(deleta_picole())
    asyncio.run(deleta_revendedor())