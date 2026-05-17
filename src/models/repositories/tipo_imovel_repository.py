from typing import List
from sqlalchemy.orm import Session
from src.errors.types.http_not_found_error import HttpNotFoundError
from src.models.interfaces.tipo_imovel_repository import TipoImovelRepositoryInterface
from src.models.entities.imovel import TipoImovel

class TipoImovelRepository(TipoImovelRepositoryInterface):
    def __init__(self, db: Session) -> None:
        self.__db_session = db


    async def inserir_tipo_imovel(self, tipo_imovel_info: dict) -> TipoImovel:
        try:            
            tipo_imovel = TipoImovel(descricao=tipo_imovel_info.get("descricao"))
            self.__db_session.add(tipo_imovel)
            self.__db_session.commit()  
            return tipo_imovel                      
        except Exception as exception:
            self.__db_session.rollback()
            raise exception
        

    async def listar_tipo_imovels(self) -> List[TipoImovel]:
        return self.__db_session.query(TipoImovel).all()        


    async def visualizar_tipo_imovel(self, tipo_imovel_id: int) -> TipoImovel:
        tipo_imovel = self.__db_session.query(TipoImovel).filter(TipoImovel.id == tipo_imovel_id).first()
        if not tipo_imovel:
            raise HttpNotFoundError("Tipo Imovel não encontrado.")
        return tipo_imovel


    async def atualizar_tipo_imovel(self, tipo_imovel_info: dict) -> TipoImovel:
        try:
            tipo_imovel = self.__db_session.query(TipoImovel).filter(TipoImovel.id == tipo_imovel_info.get("id")).first()
            if not tipo_imovel:
                raise HttpNotFoundError("Tipo Imovel não encontrado.")

            tipo_imovel.descricao = tipo_imovel_info.get("descricao")            
            self.__db_session.commit()
            
            return tipo_imovel
        except Exception as exception:
            self.__db_session.rollback()
            raise exception


    async def deletar_tipo_imovel(self, tipo_imovel_id: int) -> TipoImovel:    
        try:
            tipo_imovel = self.__db_session.query(TipoImovel).filter(TipoImovel.id == tipo_imovel_id).first()
            if not tipo_imovel:
                raise HttpNotFoundError("Tipo Imovel não encontrado.")
            
            self.__db_session.delete(tipo_imovel)
            self.__db_session.commit()
            return tipo_imovel
        except Exception as exception:
            self.__db_session.rollback()
            raise exception
        