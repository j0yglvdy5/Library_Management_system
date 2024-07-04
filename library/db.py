
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = 'sqlite:///library.db'
engine = create_engine(DATABASE_URL, echo=True)  
Session = sessionmaker(bind=engine)
Base = declarative_base()
