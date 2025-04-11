from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .database import get_db
from .models import DesertoAlimentar

router = APIRouter()

@router.get("/mapa/")
async def obter_desertos_alimentares(db: Session = Depends(get_db)):
    resultado = db.query(DesertoAlimentar).all()

    # Estruturando os dados para retorno
    dados = [
        {
            "cep": deserto.cep,
            "bairro": deserto.bairro,
            "cidade": deserto.cidade,
            "estado": deserto.estado,
            "acesso_alimentos": deserto.acesso_alimentos,
            "latitude": deserto.latitude,
            "longitude": deserto.longitude
        }
        for deserto in resultado
    ]
    
    return {"desertos": dados}
