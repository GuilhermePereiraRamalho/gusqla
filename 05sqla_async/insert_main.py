import asyncio
from conf.db_session import create_session
from models.aditivo_nutritivo import AditivoNutritivo
from models.sabor import Sabor
from models.tipo_embalagem import TipoEmbalagem
from models.tipo_picole import TipoPicole
from models.ingrediente import Ingrediente
from models.conservante import Conservante
from models.revendedor import Revendedor
from models.lote import Lote
from models.nota_fiscal import NotaFiscal
from models.picole import Picole


# tabela 1
async def insert_aditivo_nutritivo() -> AditivoNutritivo:
    print('-----------------------------')
    print('Cadastrando Aditivo Nutritivo')
    print('-----------------------------')

    nome: str = input('Informe o nome do Aditivo Nutritivo: ')
    formula_quimica: str = input('Informe a formua química do aditivo: ')

    an: AditivoNutritivo = AditivoNutritivo(nome=nome, formula_quimica=formula_quimica)

    async with create_session() as session:
        session.add(an)

        await session.commit()

        # print('--------------------------------')
        # print('Aditivo Nutritivo cadastrado com sucesso!')
        # print(f'ID: {an.id}')
        # print(f'Data de Criação: {an.data_criacao}')
        # print(f'Nome: {an.nome}')
        # print(f'Formula Química: {an.formula_quimica}')

        return an


# tabela 2
async def insert_sabor() -> None:
    print('-----------------')
    print('Cadastrando Sabor')
    print('-----------------')

    nome: str = input('Informe o nome do Sabor: ')

    sabor: Sabor = Sabor(nome=nome)

    async with create_session() as session:
        session.add(sabor)

        await session.commit()

        print('-----------------------------')
        print('Sabor cadastrado com sucesso!')
        print(f'ID: {sabor.id}')
        print(f'Data de Criação: {sabor.data_criacao}')
        print(f'Nome: {sabor.nome}')


# tabela 3
async def insert_tipo_embalagem() -> None:
    print('-----------------------------')
    print('Cadastrando Tipo de Embalagem')
    print('-----------------------------')

    nome: str = input('Informe o nome do Tipo de embalagem: ')

    te: TipoEmbalagem = TipoEmbalagem(nome=nome)

    async with create_session() as session:
        session.add(te)

        await session.commit()

    print('-----------------------------------------')
    print('Tipo de embalagem cadastrado com sucesso!')
    print(f'ID: {te.id}')
    print(f'Data de Criação: {te.data_criacao}')
    print(f'Nome: {te.nome}')


# tabela 4
async def insert_tipo_picole() -> None:
    print('--------------------------')
    print('Cadastrando Tipo de Picolé')
    print('--------------------------')

    nome: str = input('Informe o nome do Tipo de picolé: ')

    tp: TipoPicole = TipoPicole(nome=nome)

    async with create_session() as session:
        session.add(tp)

        await session.commit()

    print('--------------------------------------')
    print('Tipo de picolé cadastrado com sucesso!')
    print(f'ID: {tp.id}')
    print(f'Data de Criação: {tp.data_criacao}')
    print(f'Nome: {tp.nome}')


# tabela 5
async def insert_ingrediente() -> Ingrediente:
    print('-----------------------')
    print('Cadastrando Ingrediente')
    print('-----------------------')

    nome: str = input('Informe o nome do Ingrediente: ')

    ingrediente: Ingrediente = Ingrediente(nome=nome)

    async with create_session() as session:
        session.add(ingrediente)

        await session.commit()

        return ingrediente


# tabela 6
async def insert_conservante() -> Conservante:
    print('-----------------------')
    print('Cadastrando Conservante')
    print('-----------------------')

    nome: str = input('Informe o nome do Conservante: ')
    descricao: str = input('Informe a descrição do conservante: ')

    conservante: Conservante = Conservante(nome=nome, descricao=descricao)

    async with create_session() as session:
        session.add(conservante)

        await session.commit()

        return conservante


# tabela 7
async def insert_revendedor() -> Revendedor:
    print('----------------------')
    print('Cadastrando Revendedor')
    print('----------------------')

    cnpj: str = input('Informe o cnpj do Revendedor: ')
    razao_social: str = input('Informe a razão social do Revendedor: ')
    contato: str = input('Informe o contato do Revendedor: ')

    revendedor: Revendedor = Revendedor(cnpj=cnpj, razao_social=razao_social, contato=contato)

    async with create_session() as session:
        session.add(revendedor)

        await session.commit()

        return revendedor


# tabela 8
async def insert_lote() -> Lote:
    print('----------------')
    print('Cadastrando Lote')
    print('----------------')

    id_tipo_picole: int = int(input('Informe o ID do Tipo de Picolé: '))
    quantidade: int = int(input('Informe a quantidade de picolé: '))

    lote: Lote = Lote(id_tipo_picole=id_tipo_picole, quantidade=quantidade)

    async with create_session() as session:
        session.add(lote)

        await session.commit()

    return lote


# tabela 9
async def insert_nota_fiscal() -> None:
    print('-----------------------')
    print('Cadastrando Nota Fiscal')
    print('-----------------------')

    valor: float = float(input('Informe o valor da nota fiscal: '))
    numero_serie: str = input('Informe o número de serie: ')
    descricao: str = input('Informe a descrição: ')
    id_revendedor: int = int(input('Informe o ID do revendedor: '))

    nf: NotaFiscal = NotaFiscal(valor=valor, numero_serie=numero_serie, descricao=descricao, id_revendedor=id_revendedor)

    lote1 = await insert_lote()
    nf.lotes.append(lote1)
    
    lote2 = await insert_lote()
    nf.lotes.append(lote2)

    async with create_session() as session:
        session.add(nf)

        await session.commit()
        print('-----------------------------------')
        print('Nota Fiscal cadastrada com sucesso!')
        print(f"ID: {nf.id}")
        print(f"Data: {nf.data_criacao}")
        print(f"Valor: {nf.valor}")
        print(f"Número de Serie: {nf.numero_serie}")
        print(f"Descrição: {nf.descricao}")
        print(f"ID Revendedor: {nf.id_revendedor}")
        # print(f"Revendedor: {nf.revendedor.razao_social}")


# tabela 10
async def insert_picole() -> None:
    print('------------------')
    print('Cadastrando Picolé')
    print('------------------')

    preco: float = float(input('Informe o preço do picolé: '))
    id_sabor: int = int(input('Informe o ID do tipo do sabor: '))
    id_tipo_picole: int = int(input('Informe o ID do tipo de picolé: '))
    id_tipo_embalagem: int = int(input('Informe o ID do tipo da embalagem: '))

    picole: Picole = Picole(preco=preco, id_sabor=id_sabor, id_tipo_embalagem=id_tipo_embalagem, id_tipo_picole=id_tipo_picole)

    ingrediente1: Ingrediente = await insert_ingrediente()
    picole.ingredientes.append(ingrediente1)

    ingrediente2: Ingrediente = await insert_ingrediente()
    picole.ingredientes.append(ingrediente2)

    # tem conservantes?
    conservante: Conservante = await insert_conservante()
    picole.conservantes.append(conservante)
    
    # tem aditivo nutritivo?
    aditivo_nutritivo: AditivoNutritivo = await insert_aditivo_nutritivo()
    picole.aditivos_nutritivos.append(aditivo_nutritivo)

    async with create_session() as session:
        session.add(picole)

        await session.commit()
        print('------------------------------')
        print('Picolé cadastrado com sucesso!')
        print(f"ID: {picole.id}")
        print(f"Data: {picole.data_criacao}")
        print(f"Preço: {picole.preco}")
        # print(f"Sabor: {picole.sabor.nome}")
        # print(f"Tipo Picolé: {picole.tipo_picole.nome}")
        # print(f"Tipo Embalagem: {picole.tipo_embalagem.nome}")
        print(f"Ingredientes: {picole.ingredientes}")
        print(f"Conservantes: {picole.conservantes}")
        print(f"Aditivos Nutritivos: {picole.aditivos_nutritivos}")


if __name__ == '__main__':
    # tabela 1
    # an = asyncio.run(insert_aditivo_nutritivo())

    # print('--------------------------------')
    # print('Aditivo Nutritivo cadastrado com sucesso!')
    # print(f'ID: {an.id}')
    # print(f'Data de Criação: {an.data_criacao}')
    # print(f'Nome: {an.nome}')
    # print(f'Formula Química: {an.formula_quimica}')

    # tabela 2
    # asyncio.run(insert_sabor())

    # tabela 3
    # asyncio.run(insert_tipo_embalagem())

    # tabela 4
    # asyncio.run(insert_tipo_picole())

    # tabela 5
    # ingrediente = asyncio.run(insert_ingrediente())
    # print('-----------------------------------')
    # print('Ingrediente cadastrado com sucesso!')
    # print(f'ID: {ingrediente.id}')
    # print(f'Data de Criação: {ingrediente.data_criacao}')
    # print(f'Nome: {ingrediente.nome}')

    # tabela 6
    # conservante = asyncio.run(insert_conservante())
    # print('-----------------------------------')
    # print('Conservante cadastrado com sucesso!')
    # print(f'ID: {conservante.id}')
    # print(f'Data de Criação: {conservante.data_criacao}')
    # print(f'Nome: {conservante.nome}')
    # print(f'Descrição: {conservante.descricao}')

    # tabela 7
    # rev = asyncio.run(insert_revendedor())
    # print(f'ID: {rev.id}')
    # print(f'Data: {rev.data_criacao}')
    # print(f'CNPJ: {rev.cnpj}')
    # print(f'Razão Social: {rev.razao_social}')
    # print(f'Contato: {rev.contato}')

    # tabela 8
    # lote = asyncio.run(insert_lote())
    # print(f'ID: {lote.id}')
    # print(f'Data: {lote.data_criacao}')
    # print(f'ID Tipo Picole: {lote.id_tipo_picole}')
    # print(f'Quantidade: {lote.quantidade}')

    # tabela 9
    # asyncio.run(insert_nota_fiscal())

    # tabela 10
    asyncio.run(insert_picole())