from sqlalchemy.orm import declarative_base
import sqlalchemy as sa
from __all_models import create_table


Base = declarative_base()

create_table(Base)