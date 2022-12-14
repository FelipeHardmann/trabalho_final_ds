class Pessoa:
    '''Classe que vai setar o nome do
    Arbitro e Tecnico
    '''
    def __init__(self, nome: str) -> None:
        self.nome = nome


class Arbitro(Pessoa):
    def __init__(self, nome: str) -> None:
        super().__init__(nome)



class Tecnico(Pessoa):
    def __init__(self, nome: str) -> None:
        super().__init__(nome)


