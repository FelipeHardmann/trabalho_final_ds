import os
import platform


def limpa_tela() -> None:
    '''
    Limpa a tela independente do Sistema Operacional

    return:
        None
    '''
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def cabecalho(txt) -> str:
    '''
    Exibe um cabeçalho personalizado

    return:
        string formatada
    '''
    return f'{txt:-^50}'


def menu_principal() -> int:
    '''
    Exibe o menu principal na tela

    return:
        None
    '''
    limpa_tela()
    print(cabecalho(" MENU PRINCIPAL "))
    print(f'''
          Qual tabela você deseja 
            verificar:
            1. Seleções
            2. Técnicos
            3. Grupos
            4. Árbitros
            5. Partidas
            6. Sair
          ''')
    opcao = int(input('Opção: '))
    return opcao


def menu_secundario() -> int:
    '''
    Exibe o menu principal na tela

    return:
        None
    '''
    limpa_tela()
    print(f'''
          Qual comando você
          deseja executar:
            1. Inserir
            2. Editar
            3. Excluir
            4. Listar
          ''')
    opcao = int(input('Opção: '))
    return opcao
