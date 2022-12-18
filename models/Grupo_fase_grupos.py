from models.ModelBase import *

class Grupo(Base):
    __tablename__: str = 'grupo_fase_grupos'

    id_grupo: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    nome_grupo: str = sa.Column(sa.String(20), nullable=False)
    id_lider_grupo: int = sa.Column(sa.Integer)
    id_vice_lider_grupo: int = sa.Column(sa.Integer)
    

    def __repr__(self) -> str:
        '''Essa função retorna a representação do objeto'''
        return f''