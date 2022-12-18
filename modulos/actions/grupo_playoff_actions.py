from config.connection import (
    conecta_bd,
    abre_sessao
)

from modulos.actions.generic_actions import (inserir, listar_tabelas)

session = abre_sessao(conecta_bd())

def buscar_registro(Grupo_playoff_actions, id):
    reg = session.query(Grupo_playoff_actions).filter_by(id_grupo_playoff=id).all()
    return reg


def atualizar_registros(id, Grupo_playoff_actions):
    query = session.query(Grupo_playoff_actions).get(id)
    session.commit()
    return f'{query.id_grupo_playoff} foi atualizado com sucesso!'


def remover_registro(id, id_vencedor):
    reg = session.query(id_vencedor).filter_by(id_grupo_playoff=id).first()
    session.delete(reg)
    session.commit()
    return f'{reg} foi removido com sucesso'