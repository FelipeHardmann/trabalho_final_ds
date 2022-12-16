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
    Equipe_gol_partida,
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
                        selecao = Equipe(
                            nome = input('Digite o nome da seleção: ').strip().lower()
                        )
                        print(inserir(selecao))
                        sleep(2)