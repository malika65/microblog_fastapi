from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy import Column, String, Integer, DateTime, Boolean
from core.db import Base


class User(Base, SQLAlchemyBaseUserTable):
    name = Column(String, unique=True)
    date = Column(DateTime)




# from sqlalchemy import Column, String, Integer, DateTime, Boolean
# from core.db import Base


# class User(Base):
#     __tablename__ = 'user'
    
#     id = Column(Integer, primary_key=True, unique=True, index=True)
#     name = Column(String, unique=True)
#     email = Column(String, unique=True)
#     password = Column(String)
#     date = Column(DateTime)
#     is_active = Column(Boolean, default=False)
#     is_admin = Column(Boolean, default=False)


# users = User.__table__