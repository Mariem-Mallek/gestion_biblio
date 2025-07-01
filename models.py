import os
from dotenv import load_dotenv
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base , sessionmaker


Base = declarative_base()

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")


class Livre(Base):
    __tablename__='livres'

    id=Column(Integer,primary_key=True,autoincrement=True)
    title=Column(String,nullable=False)
    author=Column(String,nullable=False)
    year=Column(Integer)
    isbn=Column(String,unique=True,nullable=True)


engine = create_engine(DATABASE_URL, echo=True)

#Exécution des requêtes
SessionLocal = sessionmaker(bind=engine)

# Création de toutes les tables (si elles n'existent pas)
Base.metadata.create_all(bind=engine)
