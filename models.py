from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

#Base ORM
Base = declarative_base()

# Base de données SQLite locale
DATABASE_URL = "sqlite:///bibliotheque.db"

#Le modele 
class Livre(Base):
    __tablename__='livres'
    id=Column(Integer,Primary_key=True,autoincrement=True)
    titre=Column(String,nullable=False)
    author=Column(String,nullable=False)
    year=Column(Integer)
    isbn=Column(String,unique=True,nullable=True)

# Création de l'engine SQLite
engine = create_engine(DATABASE_URL, echo=True)

# Session pour exécuter des requêtes
SessionLocal = sessionmaker(bind=engine)

# Création de toutes les tables (si elles n'existent pas)
Base.metadata.create_all(bind=engine)
