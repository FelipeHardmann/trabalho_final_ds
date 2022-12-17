from models.ModelBase import *


class Tecnico(Base):
    __tablename__: str = 'tecnico'

    id_tecnico: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    nome_tecnico: str = sa.Column(sa.String(30), nullable=False)

    def __repr__(self) -> str:
        '''Essa função retorna a representação do objeto'''
        return f''