from sqlalchemy import Column, ForeignKey, Table
from models.ModelBase import *

association_table=Table(
    'association',
    Base.metadata,
    Column('id_equipe', ForeignKey('equipe.id_equipe')),
    Column('id_partida', ForeignKey('partida.id_partida'))
)