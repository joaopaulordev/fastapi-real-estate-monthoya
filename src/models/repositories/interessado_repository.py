from typing import List
from sqlalchemy.orm import Session
from src.errors.types.http_not_found_error import HttpNotFoundError
from src.models.interfaces.interessado_repository import InteressadoRepositoryInterface
from src.models.entities.imovel import Interessado, Imovel

class InteressadoRepository(InteressadoRepositoryInterface):
    def __init__(self, db: Session) -> None:
        self.__db_session = db


    async def inserir_interessado(self, interessado_info: dict) -> Interessado:
        try:
            imovel = self.__db_session.query(Imovel).filter(Imovel.id == interessado_info["imovel_id"]).first()
            if not imovel:
                raise HttpNotFoundError("Imóvel não encontrado.")
            
            interessado = Interessado(imovel=imovel, nome=interessado_info["nome"], email=interessado_info["email"], telefone=interessado_info["telefone"], estado=interessado_info["estado"], cidade=interessado_info["cidade"])
            self.__db_session.add(interessado)
            self.__db_session.commit()  
            return interessado                      
        except Exception as exception:
            self.__db_session.rollback()
            raise exception
        

    async def listar_interessados(self, imovel_id: int) -> List[Interessado]:
        imovel = self.__db_session.query(Imovel).filter(Imovel.id == imovel_id).first()
        if not imovel:
            raise HttpNotFoundError("Imóvel não encontrado.")
        
        interessados = self.__db_session.query(Interessado).filter(Interessado.imovel == imovel).all()        
        return interessados


    async def visualizar_interessado(self, interessado_id: int) -> Interessado:
        interessado = self.__db_session.query(Interessado).filter(Interessado.id == interessado_id).first()
        if not interessado:
            raise HttpNotFoundError("Interessado não encontrado.")
        return interessado


    async def atualizar_interessado(self, interessado_info: dict) -> Interessado:
        try:
            interessado = self.__db_session.query(Interessado).filter(Interessado.id == interessado_info.get("id")).first()
            if not interessado:
                raise HttpNotFoundError("Interessado não encontrado.")

            interessado.nome = interessado_info.get("nome")
            interessado.email = interessado_info.get("email")
            interessado.telefone = interessado_info.get("telefone")
            interessado.estado = interessado_info.get("estado")
            interessado.cidade = interessado_info.get("cidade")
            
            self.__db_session.commit()
            return await self.visualizar_interessado(interessado.id)
        except Exception as exception:
            self.__db_session.rollback()
            raise exception


    async def deletar_interessado(self, interessado_id: int) -> Interessado:    
        try:
            interessado = self.__db_session.query(Interessado).filter(Interessado.id == interessado_id).first()
            if not interessado:
                raise HttpNotFoundError("Interessado não encontrado.")
            
            self.__db_session.delete(interessado)
            self.__db_session.commit()
            return interessado
        except Exception as exception:
            self.__db_session.rollback()
            raise exception
        