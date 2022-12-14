import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy.orm import (
    declarative_base,
    sessionmaker
)
from datetime import datetime

# Conectando ao banco
engine = create_engine(
    url='mysql+mysqlconnector://root:admin@localhost:3306/copa',
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

    # def __repr__(self) -> str:
    #     '''Essa função retorna a representação do objeto'''
    #     return f''


class Fase(Base):
    __tablename__: str = 'fase'

    id_fase: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    nome_fase: str = sa.Column(sa.String(30), nullable=False)

    def __repr__(self) -> str:
        '''Essa função retorna a representação do objeto'''
        return f''

class Grupo(Base):
    __tablename__: str = 'grupo'

    id_grupo: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    nome_grupo: str = sa.Column(sa.String(20), nullable=False)
    fase_id: int = sa.Column(sa.Integer, sa.ForeignKey('fase.id_fase'))

    def __repr__(self) -> str:
        '''Essa função retorna a representação do objeto'''
        return f''

class Equipe(Base):
    __tablename__: str = 'equipe'

    id_equipe: int =  sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    nome_equipe: str = sa.Column(sa.String(20), nullable=False)
    tecnico_id: int = sa.Column(sa.Integer, sa.ForeignKey('tecnico.id_tecnico'))
    grupo_id: int = sa.Column(sa.Integer, sa.ForeignKey('grupo.id_grupo'))
    num_gols_equipe: int = sa.Column(sa.Integer, nullable = False)
    id_partida: int = sa.Column(sa.Integer, sa.ForeignKey('partida.id_partida'))

    def __repr__(self) -> str:
        '''Essa função retorna a representação do objeto'''
        return f''

class Partida(Base):
    __tablename__: str = 'partida'

    id_partida: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    data_hora_partida: datetime = sa.Column(sa.DateTime, nullable=False)
    local_partida: str = sa.Column(sa.String(30), nullable = False)
    id_arbitro: int = sa.Column(sa.Integer, sa.ForeignKey('arbitro.id_arbitro'))
    id_equipe: int - sa.Column(sa.Integer, sa.ForeignKey('equipe.id_equipe'))

    def __repr__(self) -> str:
        '''Essa função retorna a representação do objeto'''
        return f''

class Equipe_gol_partida(Base):
    __tablename__ = 'gol_equipe_partida'
    id_gol : int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    id_equipe: int - sa.Column(sa.Integer, sa.ForeignKey('equipe.id_equipe'))
    id_partida: int = sa.Column(sa.Integer, sa.ForeignKey('partida.id_partida'))
    num_gol: int = sa.Column(sa.Integer, nullable = False)

    def __repr__(self) -> str:
        '''Essa função retorna a representação do objeto'''
        return f''

Base.metadata.create_all(engine)