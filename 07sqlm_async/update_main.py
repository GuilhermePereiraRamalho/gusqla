from conf.db_session import create_session
from models.sabor import Sabor
from models.picole import Picole
from sqlmodel import select
import asyncio


async def select_filtro_picole(id_picole: int) -> None:
    async with create_session() as session:
        picole: Picole = await session.get(Picole, id_picole)

        if picole:
            print(f"ID: {picole.id}")
            print(f"Preço: {picole.preco}")
            print(f"Sabor: {picole.sabor.nome}")
        else:
            print('Não existe picole com o ID informado')


async def atualizar_sabor(id_sabor: int, novo_nome:str) -> None:
    async with create_session() as session:
        sabor: Sabor = await session.get(Sabor, id_sabor)

        if sabor:
            sabor.nome = novo_nome
            await session.commit()
        else:
            print(f'Não existe um sabor com ID: {id_sabor}')


async def atualizar_picole(id_picole: int, novo_preco: float, novo_sabor: int = None) -> None:
    async with create_session() as session:
        picole: Picole = await session.get(Picole, id_picole)

        if picole:
            picole.preco = novo_preco
            if novo_sabor:
                picole.id_sabor=novo_sabor
            await session.commit()
        else:
            print(f'Não existe picolé com o ID: {id_picole}')


async def atualiza_sabor():
    from select_main import select_filtro_sabor
    id_sabor = 42

    await select_filtro_sabor(id_sabor)

    await atualizar_sabor(id_sabor=id_sabor, novo_nome="Banana")

    await select_filtro_sabor(id_sabor)


async def atualiza_picole():
    id_picole = 21
    novo_preco = 6.66
    id_novo_sabor = 42

    await select_filtro_picole(id_picole=id_picole)
    await atualizar_picole(id_picole=id_picole, novo_preco=novo_preco, novo_sabor=id_novo_sabor)
    await select_filtro_picole(id_picole=id_picole)


if __name__ == '__main__':
    # asyncio.run(atualiza_sabor())
    asyncio.run(atualiza_picole())

