import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#https://martin-thoma.com/sql-connection-strings/ find connection string for mariadb here
# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:123456@localhost/northwind"


engine = sqlalchemy.create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
print(engine.table_names())

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

