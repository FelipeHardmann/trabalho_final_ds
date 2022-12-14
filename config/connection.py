import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy.orm import (
    declarative_base,
    sessionmaker
)
from datetime import datetime as dt

# Conectando ao banco
engine = create_engine(
    url = f'mysql+mysqlconnector://felipe:12345@localhost:3306/copa', 
    echo = True
)

Base = declarative_base()

class Tecnico(Base):
    __tablename__: str = 'tecnico'

    id_tecnico: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    nome_tecnico: str = sa.Column(sa.String(30), nullable=False)

    def __repr__(self) -> str:
        '''Essa função retorna a representação do objeto'''
        return f''


class Arbitro(Base):
    __tablename__: str = 'arbitro'

    id_arbitro: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    nome_arbitro: str = sa.Column(sa.String(30), nullable=False)

    def __repr__(self) -> str:
        '''Essa função retorna a representação do objeto'''
        return f''



class Fases(Base):
    __tablename__: str = 'fases'

    id_fase: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    nome_fase: str = sa.Column(sa.String(30), nullable=False)


class Grupos(Base):
    __tablename__: str = 'grupos'

    id_grupo: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    nome_grupo: str = sa.Column(sa.String(20), nullable=False)

    def __repr__(self) -> str:
        '''Essa função retorna a representação do objeto'''
        return f''


