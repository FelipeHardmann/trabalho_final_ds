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


def atualizar_registros(tbl, equipe, nova_equipe):
    query = session.query(tbl).get(equipe)
    query.nome_equipe = nova_equipe
    session.commit()
    return f'{query.nome_equipe} foi atualizado com sucesso!'


def remover_registro(tabela, nome):
    reg = session.query(tabela).filter_by(nome_equipe=nome).first()
    session.delete(reg)
    session.commit()
    return f'{reg} foi removido com sucesso'

