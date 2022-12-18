from models.ModelBase import *
from datetime import datetime

class Partida(Base):
    __tablename__: str = 'partida'

    id_partida: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    data_hora_partida: datetime = sa.Column(sa.DateTime, nullable=False)
    local_partida: str = sa.Column(sa.String(30), nullable = False)
    id_arbitro: int = sa.Column(sa.Integer, sa.ForeignKey('arbitro.id_arbitro'))
    equipe = sa.relationship('Equipe', backref = 'partida')
    def __repr__(self) -> str:
        '''Essa função retorna a representação do objeto'''
        return f''