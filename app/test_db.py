from sqlalchemy.orm import Session
from .database import engine
from .models import DesertoAlimentar

# Criar uma sessão manualmente
def testar_consulta():
    with Session(engine) as db:
        resultado = db.query(DesertoAlimentar).all()
        for registro in resultado:
            print(f"📌 {registro.cep} - {registro.bairro}, {registro.cidade}/{registro.estado}: {registro.acesso_alimentos}")

if __name__ == "__main__":
    testar_consulta()
