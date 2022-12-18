from config.connection import (
    conecta_bd,
    abre_sessao
)

from modulos.actions.generic_actions import (inserir, listar_tabelas)

session = abre_sessao(conecta_bd())

def buscar_registro(Fase, nome):
    reg = session.query(Fase).filter_by(nome_equipe=nome).all()
    return reg


def atualizar_registros(id, Fase):
    query = session.query(Fase).get(id)
    session.commit()
    return f'{query.nome_fase} foi atualizado com sucesso!'


def remover_registro(id, nome_fase):
    reg = session.query(nome_fase).filter_by(id_fase=id).first()
    session.delete(reg)
    session.commit()
    return f'{reg} foi removido com sucesso'