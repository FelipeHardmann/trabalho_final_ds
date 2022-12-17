from models.ModelBase import *

class Fase(Base):
    __tablename__: str = 'fase'

    id_fase: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    nome_fase: str = sa.Column(sa.String(30), nullable=False)

    def __repr__(self) -> str:
        '''Essa função retorna a representação do objeto'''
        return f''
