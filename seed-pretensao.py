from src.models.entities.imovel import Pretensao

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


db = create_engine("sqlite:///monthoya.db")

def get_session_db():
    try:
        Session = sessionmaker(bind=db)
        session = Session()
        yield session
    finally:
        session.close()

db_session = next(get_session_db())

venda = Pretensao(descricao="Venda")
db_session.add(venda)

locacao = Pretensao(descricao="Locação")
db_session.add(locacao)

db_session.commit()  

print("Pretensoes inseridas com sucesso!")