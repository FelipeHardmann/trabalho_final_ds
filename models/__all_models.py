from Tecnico import Tecnicox
from models import (Arbitro, Equipe, Fase, Grupo_fase_grupos, ModelBase, Partida, Tecnico)
from config.connection import conecta_bd


def create_table(Base):
    try:
        Base.metadata.create_all(conecta_bd())
    except Exception as err:
        raise err('Erro ao criar tabela')
    else:
        print('Tabela Criada com sucesso!')

create_table()