import databases
from sqlalchemy.ext.declarative import DeclarativeMeta,declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


DATABASE_URI = 'postgresql://maks:123@localhost/microblog'


engine = create_engine(DATABASE_URI, connect_args={"check_same_thread": False} )

# SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
database = databases.Database(DATABASE_URI)

Base: DeclarativeMeta = declarative_base()



