from sqlalchemy import ForeignKey
from models.ModelBase import *


class Partida(Base):
    __tablename__: str = 'gol_partida_equipe'

    id_partida: int = sa.Column(sa.Integer, ForeignKey('partida.id_partida'))
    id_equipe: int = sa.Column(sa.Integer, ForeignKey('equipe.id_equipe'))
    qtde_gols_equipe_partida: int = sa.Column(sa.Integer, nullable = False)

    def __repr__(self) -> str:
        '''Essa função retorna a representação do objeto'''
        return f''