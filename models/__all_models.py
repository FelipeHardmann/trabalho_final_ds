from Tecnico import Tecnico



def create_table():
    try:
        Base.metadata.create_all(conecta_bd())
    except Exception as err:
        raise err('Erro ao criar tabela')
    else:
        print('Tabela Criada com sucesso!')

create_table()