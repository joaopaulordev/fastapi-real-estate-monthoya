from typing import List
from sqlalchemy.orm import Session
from src.errors.types.http_not_found_error import HttpNotFoundError
from src.models.interfaces.pretensao_repository import PretensaoRepositoryInterface
from src.models.entities.imovel import Pretensao

class PretensaoRepository(PretensaoRepositoryInterface):
    def __init__(self, db: Session) -> None:
        self.__db_session = db


    async def inserir_pretensao(self, pretensao_info: dict) -> Pretensao:
        try:            
            pretensao = Pretensao(descricao=pretensao_info.get("descricao"))
            self.__db_session.add(pretensao)
            self.__db_session.commit()  
            return pretensao                      
        except Exception as exception:
            self.__db_session.rollback()
            raise exception
        

    async def listar_pretensoes(self) -> List[Pretensao]:
        return self.__db_session.query(Pretensao).all()        


    async def visualizar_pretensao(self, pretensao_id: int) -> Pretensao:
        pretensao = self.__db_session.query(Pretensao).filter(Pretensao.id == pretensao_id).first()
        if not pretensao:
            raise HttpNotFoundError("Pretensão não encontrada.")
        return pretensao


    async def atualizar_pretensao(self, pretensao_info: dict) -> Pretensao:
        try:
            pretensao = self.__db_session.query(Pretensao).filter(Pretensao.id == pretensao_info.get("id")).first()
            if not pretensao:
                raise HttpNotFoundError("Pretensão não encontrada.")

            pretensao.descricao = pretensao_info.get("descricao")            
            self.__db_session.commit()
            
            return pretensao
        except Exception as exception:
            self.__db_session.rollback()
            raise exception


    async def deletar_pretensao(self, pretensao_id: int) -> Pretensao:    
        try:
            pretensao = self.__db_session.query(Pretensao).filter(Pretensao.id == pretensao_id).first()
            if not pretensao:
                raise HttpNotFoundError("Pretensão não encontrada.")
            
            self.__db_session.delete(pretensao)
            self.__db_session.commit()
            return pretensao
        except Exception as exception:
            self.__db_session.rollback()
            raise exception
        