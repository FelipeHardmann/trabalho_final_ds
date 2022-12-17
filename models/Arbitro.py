from models.ModelBase import *

class Arbitro(Base):
    __tablename__: str = 'arbitro'

    id_arbitro: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    nome_arbitro: str = sa.Column(sa.String(30), nullable=False)

    # def __repr__(self) -> str:
    #     '''Essa função retorna a representação do objeto'''
    #     return f''