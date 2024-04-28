from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://user:password@db/testdb"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Task(Base):  
    __tablename__ = "tasks"  

    id = Column(Integer, primary_key=True, index=True)
    task = Column(String(100), index=True)
    description = Column(String(100), index=True)