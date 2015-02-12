from sqlacademy import create_engine
from sqlacademy.orm import sessionmaker
from sqlacademy.ext.declarative import declarative_base

from blog import app

engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"])
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()