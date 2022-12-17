from models.ModelBase import *

class Equipe(Base):
    __tablename__: str = 'equipe'

    id_equipe: int =  sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    nome_equipe: str = sa.Column(sa.String(20), nullable=False)
    tecnico_id: int = sa.Column(sa.Integer, sa.ForeignKey('tecnico.id_tecnico'))
    grupo_id: int = sa.Column(sa.Integer, sa.ForeignKey('grupo.id_grupo'))

    def __repr__(self) -> str:
        '''Essa função retorna a representação do objeto'''
        return f''