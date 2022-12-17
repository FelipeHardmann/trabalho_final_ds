'''
Arquivo para cadastrar, Listar, Remover, Procurar e Atualizar
'''

from config.connection import (
    conecta_bd,
    abre_sessao
)

session = abre_sessao(conecta_bd())

def buscar_registro(tabela, nome):
    reg = session.query(tabela).filter_by(name=nome).all()
    return reg


def inserir(nome):
    session.add(nome)
    session.commit()
    return f'{nome} cadstrado com Sucesso'


def listar_tabelas(tabela):
    query_tabela = session.query(tabela).all()
    return query_tabela


def atualizar_registros(tabela, nome, opcao, campo):
    query = session.query(tabela).get(nome)
    match opcao:
        case 'tecnico':
            query.nome_tecnico = campo
        case 'selecao':
            query.nome_equipe = campo
        case 'arbitro':
            query.nome_arbitro = campo
        case 'grupo':
            query.nome_grupo = campo
        case '':
            ''

    session.commit()
    return f'{query.nome} foi atualizado'


def remover_registro(tabela, nome):
    reg = session.query(tabela).filter_by(name=nome).first()
    session.delete(reg)
    session.commit()
    return f'{reg.nome} foi removido com sucesso'

