'''
Arquivo para cadastrar, Listar
'''

#Funlções de requisição ao banco genéricas (que todas as tabelas podem usar)
#Dentro de cada action de cada tabela, tem requisição ao banco usando seu modelo para tais requisições

from config.connection import (
    conecta_bd,
    abre_sessao
)

session = abre_sessao(conecta_bd())

def inserir(nome):
    session.add(nome)
    session.commit()
    return f'{nome} cadstrado com Sucesso'


def listar_tabelas(tabela):
    query_tabela = session.query(tabela).all()
    return query_tabela
