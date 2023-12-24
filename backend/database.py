from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL
import os


DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_SERVICE_HOST = os.environ.get('DB_SERVICE_HOST')
DB_SERVICE_PORT = os.environ.get('DB_SERVICE_PORT')
DB_DATABASE = os.environ.get('DB_DATABASE')

print(DB_SERVICE_HOST)
print(DB_SERVICE_PORT)


if DB_SERVICE_HOST:
    SQLALCHEMY_DATABASE_URL = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_SERVICE_HOST}:{DB_SERVICE_PORT}/{DB_DATABASE}'
else:
    SQLALCHEMY_DATABASE_URL = 'sqlite:///./test.db'



#SQLALCHEMY_DATABASE_URL = f'postgresql://:postgresuser@20.241.174.75:5432/postgresdb'

print(SQLALCHEMY_DATABASE_URL)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
