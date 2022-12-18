from config.connection import (
    conecta_bd,
    abre_sessao
)

from modulos.actions.generic_actions import (inserir, listar_tabelas)

session = abre_sessao(conecta_bd())

def buscar_registro(tabela, nome):
    reg = session.query(tabela).filter_by(nome_arbitro=nome).all()
    return reg


def atualizar_registros(id, Arbitro):
    query = session.query(Arbitro).get(id)
    session.commit()
    return f'{query.nome_equipe} foi atualizado com sucesso!'


def remover_registro(id, nome_tecnico):
    reg = session.query(nome_tecnico).filter_by(id_tecnico=id).first()
    session.delete(reg)
    session.commit()
    return f'{reg} foi removido com sucesso'