from models.ModelBase import *

class Equipe(Base):
    __tablename__: str = 'equipe'

    id_equipe: int =  sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    nome_equipe: str = sa.Column(sa.String(20), nullable=False)
    saldo_gols_equipe: int = sa.Column(sa.Integer, nullable = False)
    num_vitorias_equipe: int = sa.Column(sa.Integer, nullable = False)
    pontos_fase_grupo: int = sa.Column(sa.Integer, nullable = False)
    tecnico_id: int = sa.Column(sa.Integer, sa.ForeignKey('tecnico.id_tecnico'))
    grupo_id: int = sa.Column(sa.Integer, sa.ForeignKey('grupo.id_grupo'))
    id_grupo_playoff: int = sa.Column(sa.Integer, sa.ForeignKey('grupo_playoff.id_grupo_playoff'))
    partida = sa.relationship('Partida', backref = 'equipe')
    
    def __repr__(self) -> str:
        '''Essa função retorna a representação do objeto'''
        return f''