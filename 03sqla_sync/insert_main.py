from conf.db_session import create_session
from models.aditivo_nutritivo import AditivoNutritivo
from models.sabor import Sabor
from models.tipo_embalagem import TipoEmbalagem
from models.tipo_picole import TipoPicole
from models.ingrediente import Ingrediente
from models.conservante import Conservante
from models.revendedor import Revendedor


# tabela 1
def insert_aditivo_nutritivo() -> None:
    print('--------------------------------')
    print('Cadastrando Aditivo Nutritivo...')
    print('--------------------------------')

    nome: str = input('Informe o nome do Aditivo Nutritivo: ')
    formula_quimica: str = input('Informe a formua química do aditivo: ')

    an: AditivoNutritivo = AditivoNutritivo(nome=nome, formula_quimica=formula_quimica)

    with create_session() as session:
        session.add(an)

        session.commit()

    print('--------------------------------')
    print('Aditivo Nutritivo cadastrado com sucesso!')
    print(f'ID: {an.id}')
    print(f'Data de Criação: {an.data_criacao}')
    print(f'Nome: {an.nome}')
    print(f'Formula Química: {an.formula_quimica}')


# tabela 2
def insert_sabor() -> None:
    print('-----------------')
    print('Cadastrando Sabor')
    print('-----------------')

    nome: str = input('Informe o nome do Sabor: ')

    sabor: Sabor = Sabor(nome=nome)

    with create_session() as session:
        session.add(sabor)

        session.commit()

    print('-----------------------------')
    print('Sabor cadastrado com sucesso!')
    print(f'ID: {sabor.id}')
    print(f'Data de Criação: {sabor.data_criacao}')
    print(f'Nome: {sabor.nome}')


# tabela 3
def insert_tipo_embalagem() -> None:
    print('-----------------------------')
    print('Cadastrando Tipo de Embalagem')
    print('-----------------------------')

    nome: str = input('Informe o nome do Tipo de embalagem: ')

    te: TipoEmbalagem = TipoEmbalagem(nome=nome)

    with create_session() as session:
        session.add(te)

        session.commit()

    print('-----------------------------------------')
    print('Tipo de embalagem cadastrado com sucesso!')
    print(f'ID: {te.id}')
    print(f'Data de Criação: {te.data_criacao}')
    print(f'Nome: {te.nome}')


# tabela 4
def insert_tipo_picole() -> None:
    print('--------------------------')
    print('Cadastrando Tipo de Picolé')
    print('--------------------------')

    nome: str = input('Informe o nome do Tipo de picolé: ')

    tp: TipoPicole = TipoPicole(nome=nome)

    with create_session() as session:
        session.add(tp)

        session.commit()

    print('--------------------------------------')
    print('Tipo de picolé cadastrado com sucesso!')
    print(f'ID: {tp.id}')
    print(f'Data de Criação: {tp.data_criacao}')
    print(f'Nome: {tp.nome}')


# tabela 5
def insert_ingrediente() -> None:
    print('-----------------------')
    print('Cadastrando Ingrediente')
    print('-----------------------')

    nome: str = input('Informe o nome do Ingrediente: ')

    ingrediente: Ingrediente = Ingrediente(nome=nome)

    with create_session() as session:
        session.add(ingrediente)

        session.commit()

    print('-----------------------------------')
    print('Ingrediente cadastrado com sucesso!')
    print(f'ID: {ingrediente.id}')
    print(f'Data de Criação: {ingrediente.data_criacao}')
    print(f'Nome: {ingrediente.nome}')


# tabela 6
def insert_conservante() -> None:
    print('-----------------------')
    print('Cadastrando Conservante')
    print('-----------------------')

    nome: str = input('Informe o nome do Conservante: ')
    descricao: str = input('Informe a descrição do conservante: ')

    conservante: Conservante = Conservante(nome=nome, descricao=descricao)

    with create_session() as session:
        session.add(conservante)

        session.commit()

    print('-----------------------------------')
    print('Conservante cadastrado com sucesso!')
    print(f'ID: {conservante.id}')
    print(f'Data de Criação: {conservante.data_criacao}')
    print(f'Nome: {conservante.nome}')
    print(f'Descrição: {conservante.descricao}')


# tabela 7
def insert_revendedor() -> Revendedor:
    print('----------------------')
    print('Cadastrando Revendedor')
    print('----------------------')

    cnpj: str = input('Informe o cnpj do Revendedor: ')
    razao_social: str = input('Informe a razão social do Revendedor: ')
    contato: str = input('Informe o contato do Revendedor: ')

    revendedor: Revendedor = Revendedor(cnpj=cnpj, razao_social=razao_social, contato=contato)

    with create_session() as session:
        session.add(revendedor)

        session.commit()

    return revendedor


if __name__ == '__main__':
    # tabela 1
    # insert_aditivo_nutritivo()

    # tabela 2
    # insert_sabor()

    # tabela 3
    # insert_tipo_embalagem()

    # tabela 4
    # insert_tipo_picole()

    # tabela 5
    # insert_ingrediente()

    # tabela 6
    # insert_conservante()

    # tabela 7
    rev = insert_revendedor()
    print(f'ID: {rev.id}')
    print(f'Data: {rev.data_criacao}')
    print(f'CNPJ: {rev.cnpj}')
    print(f'Razão Social: {rev.razao_social}')
    print(f'Contato: {rev.contato}')