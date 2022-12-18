from sqlalchemy import ForeignKey
from models.ModelBase import *

class Partida(Base):
    __tablename__: str = 'grupo_playoff'
    id_grupo_playoff: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    id_vencedor_grupo_playoff: int = sa.Column(sa.Integer)
    id_fase: int = sa.Column(sa.Integer, ForeignKey('fase.id_fase'))
    
    def __repr__(self) -> str:
        '''Essa função retorna a representação do objeto'''
        return f''