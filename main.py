from modulos.actions.arbitro_actions import atualizar_registros, remover_registro
from modulos.menu import (
    menu_principal,
    limpa_tela,
    menu_secundario,
    cabecalho
)
from time import sleep
from modulos.actions.generic_actions import (
    inserir,
    listar_tabelas
)

from models.__all_models import (Arbitro, Equipe, Grupo_playoff, Fase, Grupo_fase_grupos, Gol_equipe_partida, Tecnico, Partida)

import sys


def verifyEquipe(): #Função verifica se equipe já existe
    nameEquipe = str(input('Digite o nome da equipe: '))
    nameEquipeTrated = f"('{nameEquipe}',)"
    for element in listar_tabelas(Equipe.nome_equipe): #Falta importar os models
        if(nameEquipeTrated == str(element)):
            nameEquipe = str(input('Equipe já existente, digite outro nome: '))
    selecao = Equipe(
        tecnico_id = int(input('Digite o ID do técnico: ')),
        grupo_id = int(input('Digite o ID do grupo: ')),
        nome_equipe = nameEquipe
    )
    return selecao


#Menu Principal

if __name__ == '__main__':
    while True: 
        match menu_principal():
            case 1:
                limpa_tela() 
                match menu_secundario():
                    case 1:
                        limpa_tela()
                       # print(element.nome_equipe)
                        inserir(verifyEquipe()) #Passa na função inserir o retorno da função verify
                        sleep(2)
                    case 2:
                        # Está com erro
                        limpa_tela()
                        print(cabecalho(' Atualizar registro '))
                        #Retorna a lista de todas as seleçoes para o usuario escolher qual deseja atualizar
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
                        #Mesmo objetivo do laço do case 2
                        for equipe in listar_tabelas(Equipe):
                            print(f'{equipe.nome_equipe}')
                        equipe = input('Qual seleção você deseja remover? ').lower()
                        print(remover_registro(Equipe, equipe))