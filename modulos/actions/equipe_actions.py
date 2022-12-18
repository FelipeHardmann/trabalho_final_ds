from config.connection import (
    conecta_bd,
    abre_sessao
)

from modulos.actions.generic_actions import (inserir, listar_tabelas)

session = abre_sessao(conecta_bd())

def buscar_registro(Equipe, nome):
    reg = session.query(Equipe).filter_by(nome_equipe=nome).all()
    return reg


def atualizar_registros(id, Equipe):
    query = session.query(Equipe).get(id)
    session.commit()
    return f'{query.nome_equipe} foi atualizado com sucesso!'


def remover_registro(id, nome_equipe):
    reg = session.query(nome_equipe).filter_by(id_equipe=id).first()
    session.delete(reg)
    session.commit()
    return f'{reg} foi removido com sucesso'