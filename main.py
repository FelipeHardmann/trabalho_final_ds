from modulos.menu import (
    menu_principal,
    limpa_tela,
    menu_secundario,
    cabecalho
)
from time import sleep
from config.table import (
    create_table,
    Tecnico,
    Arbitro,
    Equipe,
    Grupo,
    Partida,
    Fase
)
from modulos.actions import (
    inserir,
    buscar_registro,
    atualizar_registros,
    remover_registro,
    listar_tabelas
)
import sys

if __name__ == '__main__':
    while True:
        match menu_principal():
            case 1:
                limpa_tela() 
                match menu_secundario():
                    case 1:
                        limpa_tela()
                        for element in listar_tabelas(Equipe):
                            print(element.nome_equipe)
                        selecao = Equipe(
                            nome_equipe = input('Digite o nome da seleção: ').strip().lower(),
                            tecnico_id = int(input('ID: ')),
                            grupo_id = int(input('ID: '))
                        )
                        print(inserir(selecao))
                        sleep(2)
                    case 2:
                        # Está com erro
                        limpa_tela()
                        print(cabecalho(' Atualizar registro '))
                        for equipe in listar_tabelas(Equipe):
                            print(f'{equipe.id_equipe} {equipe.nome_equipe}')
                        escolha = int(input('Qual seleção você deseja atualizar: '))
                        nova_selecao = input('Nova seleção: ')
                        selecao = Equipe(
                            print(atualizar_registros(Equipe, equipe, nova_selecao))
                        )
                    case 3:
                        limpa_tela()
                        print(cabecalho(' Excluindo Seleção '))
                        for selecao in listar_tabelas(Equipe):
                            print(f'{selecao.nome_equipe}')
                        equipe = input('Qual seleção você deseja remover? ').lower()
                        print(remover_registro(Equipe, equipe))
                        
                    