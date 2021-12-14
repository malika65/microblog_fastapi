import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


DATABASE_URI = 'postgresql://maks:123@localhost/microblog'


engine = create_engine(DATABASE_URI)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()



