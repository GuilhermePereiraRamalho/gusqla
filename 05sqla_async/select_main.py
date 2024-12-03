import asyncio
from typing import List
from sqlalchemy import func
from sqlalchemy.future import select
from conf.helpers import formata_data
from conf.db_session import create_session
# select simples
from models.aditivo_nutritivo import AditivoNutritivo
from models.sabor import Sabor
from models.revendedor import Revendedor
# select compostos/complexos
from models.picole import Picole


## Select simples -> SELECT * FROM aditivos_nutritivos
async def select_todos_aditivos_nutritivos() -> None:
    async with create_session() as session:
        query = select(AditivoNutritivo)
        aditivos_nutritivos: List[AditivoNutritivo] = await session.execute(query)
        aditivos_nutritivos = aditivos_nutritivos.scalars().all()

        """
        aditivos_nutritivos: List[AditivoNutritivo] = await session.execute(select(AditivoNutritivo)).scalars().all()
        """

        for an in aditivos_nutritivos:
            print(f'ID: {an.id}')
            print(f'Data: {formata_data(an.data_criacao)}')
            print(f'Nome: {an.nome}')
            print(f'Fórmula Química: {an.formula_quimica}')


async def select_filtro_sabor(id_sabor: int) -> None:
    async with create_session() as session:
        query = select(Sabor).filter(Sabor.id == id_sabor)
        # query = select(Sabor).where(Sabor.id == id_sabor)

        result = await session.execute(query)

        # forma 1
        # sabor: Sabor = result.scalars().first()

        # forma 2
        # sabor: Sabor = result.scalars().one_or_none()

        # forma 3
        # sabor: Sabor = result.scalars().one()

        # forma 4
        sabor: Sabor = result.scalar_one_or_none()

        print(f"ID: {sabor.id}")
        print(f"Data: {formata_data(sabor.data_criacao)}")
        print(f"Nome: {sabor.nome}")


async def select_complexo_picole() -> None:
    async with create_session() as session:
        query = select(Picole)
        result = await session.execute(query)
        picoles: List[Picole] = result.scalars().unique().all()

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


async def select_order_by_sabor() -> None:
    async with create_session() as session:
        query = select(Sabor).order_by(Sabor.data_criacao.desc())
        result = await session.execute(query)
        sabores: List[Sabor] = result.scalars().all()

        for sabor in sabores:
            print(f"ID: {sabor.id}")
            print(f"Nome: {sabor.nome}")


async def select_group_by_picole() -> None:
    async with create_session() as session:
        query = select(Picole).group_by(Picole.id, Picole.id_tipo_picole)
        result = await session.execute(query)
        picoles: List[Picole] = result.scalars().unique().all()

        for picole in picoles:
            print(f'ID: {picole.id}')
            print(f'Tipo Picole: {picole.tipo_picole.nome}')
            print(f'Sabor: {picole.sabor.nome}')
            print(f'Preço: {picole.preco}')


async def select_limit() -> None:
    async with create_session() as session:
        query = select(Sabor).limit(25)
        result = await session.execute(query)
        sabores: List[Sabor] = result.scalars()

        for sabor in sabores:
            print(f'ID: {sabor.id}')
            print(f'Nome: {sabor.nome}')


async def select_count_revendedor() -> None:
    async with create_session() as session:
        query = select(func.count(Revendedor.id))
        result = await session.execute(query)
        qtd: int =  result.scalar()

        print(f'Quatidade de revendedores: {qtd}')


async def select_agregacao() -> None:
    async with create_session() as session:
        query = select(
            func.sum(Picole.preco).label('soma'),
            func.avg(Picole.preco).label('media'),
            func.min(Picole.preco).label('mais_barato'),
            func.max(Picole.preco).label('mais_caro'),
        )
        result = await session.execute(query)
        resultado = result.all()


        print(f"Resultado: {resultado}")

        print(f'A soma de todos os picolés é: {resultado[0][0]}')
        print(f'A média de todos os picolés é: {resultado[0][1]}')
        print(f'O picolé mais barato é: {resultado[0][2]}')
        print(f'O picolé mais caro é: {resultado[0][3]}')



if __name__ == '__main__':
    # asyncio.run(select_todos_aditivos_nutritivos())
    # asyncio.run(select_filtro_sabor(21))
    # asyncio.run(select_complexo_picole())
    # asyncio.run(select_order_by_sabor())
    # asyncio.run(select_group_by_picole())
    # asyncio.run(select_limit())
    # asyncio.run(select_count_revendedor())
    asyncio.run(select_agregacao())