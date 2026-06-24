from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from src.main.server.server import SECRET_KEY, ALGORITHM, oauth2_schema
from fastapi import Depends, HTTPException
from src.models.entities.imovel import Usuario
from jose import jwt, JWTError

db = create_engine("sqlite:///monthoya.db")

def get_session_db():
    try:
        Session = sessionmaker(bind=db)
        session = Session()
        yield session
    finally:
        session.close()


def check_token(token: str = Depends(oauth2_schema), session: Session = Depends(get_session_db)):
    try:
        dic_info = jwt.decode(token, SECRET_KEY, ALGORITHM)
        id_usuario = int(dic_info.get("sub"))
    except JWTError:
        raise HTTPException(status_code=401, detail="Acesso Negado, verifique a validade do token")

    usuario = session.query(Usuario).filter(Usuario.id==id_usuario).first()
    if not usuario:
        raise HTTPException(status_code=401, detail="Acesso Inválido")
    return usuario