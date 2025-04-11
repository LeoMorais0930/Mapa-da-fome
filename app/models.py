from sqlalchemy import Column, Integer, String, Float
from .database import Base

class DesertoAlimentar(Base):
    __tablename__ = "desertos_alimentares"

    id = Column(Integer, primary_key=True, index=True)
    cep = Column(String, index=True)
    bairro = Column(String)
    cidade = Column(String)
    estado = Column(String)
    acesso_alimentos = Column(String)
    latitude = Column(Float)  # ← Certifique-se de que está definido!
    longitude = Column(Float)  # ← Certifique-se de que está definido!
