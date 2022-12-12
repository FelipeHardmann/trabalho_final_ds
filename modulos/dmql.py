class DML:
    def __init__(self, conn, qry):
        self.__conn = conn
        self.__cursor = conn.cursor()
        self.__query = qry

    def insere_registros(self, tabela, nome):
        if self.verifica_nome(tabela, nome):
            query = f'INSERT INTO {tabela} VALUES ("{nome}")'
            self.__cursor.execute([query])
            self.__conn.commit()
            return True
        return False

    def verifica_nome(self, tabela, login):
        self.lista_logins = [ login_name[0] for login_name in self.__query.busca_registros(tabela)]
        if login in self.lista_logins:
            print(f'Nome - {login} - já existe. Digite outro...')
            return False
        return True

    def atualizar_registro(self, tabela, campo, pos1, pos2, valor):
        registros = self.__query.busca_registros(tabela)
        query = f'UPDATE {tabela} SET {campo}="{valor}" WHERE {campo}="{registros[pos1][pos2]}"'
        self.__cursor.execute(query)
        self.__conn.commit()
        return True

    def remover_registro(self, tabela, pos):
        registros = self.__query.busca_registros(tabela)
        query = f'DELETE FROM {tabela}  WHERE LOGIN="{registros[pos][0]}"'
        self.__cursor.execute(query)
        self.__conn.commit()
        return True


class DQL:
    def __init__(self, conn):
        self.__conn = conn
        self.__cursor = conn.cursor()

    def busca_registros(self, tabela, colunas='*'):
        self.__cursor.execute(f'SELECT {colunas} FROM {tabela}')
        return self.__cursor.fetchall()