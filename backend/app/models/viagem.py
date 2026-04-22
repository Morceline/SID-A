from sqlalchemy import Column, Integer, String
from app.database.connection import Base

class Viagem(Base):
    __tablename__ = "viagens"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    status = Column(String)  # ativa, finalizada