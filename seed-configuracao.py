from src.models.entities.imovel import Configuracao

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

configDestaque= Configuracao(descricao="Quantidade de imóveis em destaque que aparecerá na página home.", quantidade=3)
db_session.add(configDestaque)

configLancamento= Configuracao(descricao="Quantidade de imóveis em lançamento que aparecerá na página home.", quantidade=3)
db_session.add(configLancamento)

configMaisVisualizados= Configuracao(descricao="Quantidade de imóveis mais visualizados que aparecerá na página home.", quantidade=3)
db_session.add(configMaisVisualizados)

db_session.commit()  

print("Cofiguracoes inseridas com sucesso!")