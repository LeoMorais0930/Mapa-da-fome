from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Configuração da conexão com o banco Oracle
DATABASE_URL = "oracle+oracledb://system:093003@DESKTOP-KHKU2NH:1521/FREE"

engine = create_engine(
    DATABASE_URL,
    pool_size=10,
    max_overflow=5,
    pool_timeout=30,
    echo=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def criar_tabelas():
    Base.metadata.create_all(bind=engine)
    print("Tabelas criadas com sucesso.")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Inicialização do banco e inserção de dados
if __name__ == "__main__":
    try:
        with engine.connect():
            print("Conexão com Oracle estabelecida.")

        criar_tabelas()

        from .crud import adicionar_dados

        with SessionLocal() as db:
            adicionar_dados(db)

        print("Dados de teste inseridos.")

    except Exception as e:
        print(f"Erro ao conectar ao Oracle: {e}")
