import sys
from config.connection import Connection
from dotenv import load_dotenv
from modulos.menu import Menu, MenuSecundario
from modulos.dmql import (
    DQL, DML
)

path = load_dotenv('./config/.env')
cnx = Connection()

conn = cnx.connect(path)
dql = DQL(conn)
dml = DML(conn, dql)
menu = Menu()
menusecundario = MenuSecundario()

while True:
    print(menu.menu_principal())
    escolha = int(input('Escolha: '))

    match escolha:
        case 1:
            print(menusecundario.menu_secundario())
            escolha2 = int(input('Escolha: '))
            match escolha2:
                case 1:
                    for selecoes, nome in dql.busca_registros('equipe'):
                        print(f'{selecoes:<10}: {nome}')
                case 2:
                    nomeSelecao = input('Digite o nome da Seleção: ').title()
                    if not dml.verifica_nome('equipe', nomeSelecao):
                        print(f'Hello {nomeSelecao}')
                        nomeSelecao = input('Digite o nome da Seleção: ').title()
                        dml.insere_registros('equipe', nomeSelecao)
                        print(f'{nomeSelecao} inserido com sucesso')
