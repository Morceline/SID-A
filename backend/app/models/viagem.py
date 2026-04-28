from sqlalchemy import Column, Integer, String, ForeignKey
from app.database.connection import Base

class Viagem(Base):
    __tablename__ = "viagens"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))