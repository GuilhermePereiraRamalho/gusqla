from sqlalchemy.ext.declarative import declarative_base


ModelBase = declarative_base()
ModelBase.__allow_unmapped__ = True