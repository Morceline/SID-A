from sqlalchemy import Column, Integer, Float, String, ForeignKey
from app.database.connection import Base

class Evento(Base):
    __tablename__ = "eventos"

    id = Column(Integer, primary_key=True, index=True)
    viagem_id = Column(Integer, ForeignKey("viagens.id"))
    latitude = Column(Float)
    longitude = Column(Float)
    tipo = Column(String)  # inicio, posicao, parada, entrega