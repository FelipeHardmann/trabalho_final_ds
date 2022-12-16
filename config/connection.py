from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

engine = None

def conecta_bd():
    try:
        global engine
        if engine:
            return engine
        engine = create_engine(
        url='mysql+mysqlconnector://felipe:12345@localhost:3306/copa',
        echo = True
        )
    except Exception as err:
        raise err('Erro ao conectar')
    else:
        return engine
        
def abre_sessao(eng):
    try:
        Session = sessionmaker(bind = eng)
    except Exception as err:
        raise err('Não foi possível abrir a sessão')
    else:
        session = Session()
        return session
