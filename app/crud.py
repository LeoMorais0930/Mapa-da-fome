from sqlalchemy.orm import Session
from .models import DesertoAlimentar

def adicionar_dados(db: Session):
    dados_exemplo = [
        DesertoAlimentar(cep="01001000", bairro="Sé", cidade="São Paulo", estado="SP", acesso_alimentos="Baixo"),
        DesertoAlimentar(cep="20040002", bairro="Centro", cidade="Rio de Janeiro", estado="RJ", acesso_alimentos="Médio"),
        DesertoAlimentar(cep="30140071", bairro="Savassi", cidade="Belo Horizonte", estado="MG", acesso_alimentos="Alto"),
    ]

    db.add_all(dados_exemplo)
    db.commit()
    print("✅ Dados de teste inseridos com sucesso!")
