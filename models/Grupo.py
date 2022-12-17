from models.ModelBase import *

class Grupo(Base):
    __tablename__: str = 'grupo'

    id_grupo: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    nome_grupo: str = sa.Column(sa.String(20), nullable=False)
    fase_id: int = sa.Column(sa.Integer, sa.ForeignKey('fase.id_fase'))

    def __repr__(self) -> str:
        '''Essa função retorna a representação do objeto'''
        return f''