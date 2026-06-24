from src.models.entities.imovel import Usuario
from passlib.context import CryptContext

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


db = create_engine("sqlite:///monthoya.db")

def get_session_db():
    try:
        Session = sessionmaker(bind=db)
        session = Session()
        yield session
    finally:
        session.close()

db_session = next(get_session_db())

senha_criptografada = bcrypt_context.hash("12345678")
novo_usuario = Usuario("john", "john@gmail.com", senha_criptografada, True, True)
db_session.add(novo_usuario)
db_session.commit()

print("Usuário inserido com sucesso!")