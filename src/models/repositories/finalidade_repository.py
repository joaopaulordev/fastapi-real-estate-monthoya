from typing import List
from sqlalchemy.orm import Session
from src.errors.types.http_not_found_error import HttpNotFoundError
from src.models.interfaces.finalidade_repository import FinalidadeRepositoryInterface
from src.models.entities.imovel import Finalidade, Imovel

class FinalidadeRepository(FinalidadeRepositoryInterface):
    def __init__(self, db: Session) -> None:
        self.__db_session = db


    async def inserir_finalidade(self, finalidade_info: dict) -> Finalidade:
        try:            
            finalidade = Finalidade(descricao=finalidade_info.get("descricao"))
            self.__db_session.add(finalidade)
            self.__db_session.commit()  
            return finalidade                      
        except Exception as exception:
            self.__db_session.rollback()
            raise exception
        

    async def listar_finalidades(self) -> List[Finalidade]:
        return self.__db_session.query(Finalidade).all()        


    async def visualizar_finalidade(self, finalidade_id: int) -> Finalidade:
        finalidade = self.__db_session.query(Finalidade).filter(Finalidade.id == finalidade_id).first()
        if not finalidade:
            raise HttpNotFoundError("Finalidade não encontrada.")
        return finalidade


    async def atualizar_finalidade(self, finalidade_info: dict) -> Finalidade:
        try:
            finalidade = self.__db_session.query(Finalidade).filter(Finalidade.id == finalidade_info.get("id")).first()
            if not finalidade:
                raise HttpNotFoundError("Finalidade não encontrada.")

            finalidade.descricao = finalidade_info.get("descricao")
            
            self.__db_session.commit()
            return await self.visualizar_finalidade(finalidade.id)
        except Exception as exception:
            self.__db_session.rollback()
            raise exception


    async def deletar_finalidade(self, finalidade_id: int) -> Finalidade:    
        try:
            finalidade = self.__db_session.query(Finalidade).filter(Finalidade.id == finalidade_id).first()
            if not finalidade:
                raise HttpNotFoundError("Finalidade não encontrada.")
            
            self.__db_session.delete(finalidade)
            self.__db_session.commit()
            return finalidade
        except Exception as exception:
            self.__db_session.rollback()
            raise exception
        