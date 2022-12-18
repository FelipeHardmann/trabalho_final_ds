from config.connection import (
    conecta_bd,
    abre_sessao
)

from modulos.actions.generic_actions import (inserir, listar_tabelas)

session = abre_sessao(conecta_bd())

def buscar_registro(Grupo_fase_grupos, nome):
    reg = session.query(Grupo_fase_grupos).filter_by(nome_grupo=nome).all()
    return reg


def atualizar_registros(id, Grupo_fase_grupos): #Recebe o id e o registro para sobrescrever o antigo
    query = session.query(Grupo_fase_grupos).get(id)
    session.commit()
    return f'{query.nome_grupo_} foi atualizado com sucesso!'


def remover_registro(id, nome_grupo):
    reg = session.query(nome_grupo).filter_by(id_tecnico=id).first()
    session.delete(reg)
    session.commit()
    return f'{reg} foi removido com sucesso'