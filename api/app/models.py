import os
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_port = os.environ.get("DB_PORT", 8181)
db_user = os.environ.get("DB_USER", "user")
db_pwd = os.environ.get("DB_PWD", "password")
db_host = os.environ.get("DB_HOST", "db")
db_name = os.environ.get("DB_NAME", "testdb")

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{db_user}:{db_pwd}@{db_host}/{db_name}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Task(Base):  
    __tablename__ = "tasks"  

    id = Column(Integer, primary_key=True, index=True)
    task = Column(String(100), index=True)
    description = Column(String(100), index=True)