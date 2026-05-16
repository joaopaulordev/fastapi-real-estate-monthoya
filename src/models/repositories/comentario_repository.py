from typing import List
from sqlalchemy.orm import Session
from src.errors.types.http_not_found_error import HttpNotFoundError
from src.models.interfaces.comentario_repository import ComentarioRepositoryInterface
from src.models.entities.imovel import Comentario, Imovel

class ComentarioRepository(ComentarioRepositoryInterface):
    def __init__(self, db: Session) -> None:
        self.__db_session = db


    async def inserir_comentario(self, comentario_info: dict) -> Comentario:
        try:
            imovel = self.__db_session.query(Imovel).filter(Imovel.id == comentario_info["imovel_id"]).first()
            if not imovel:
                raise HttpNotFoundError("Imóvel não encontrado.")
            
            comentario = Comentario(imovel=imovel, texto=comentario_info["texto"])
            self.__db_session.add(comentario)
            self.__db_session.commit()  
            return comentario                      
        except Exception as exception:
            self.__db_session.rollback()
            raise exception
        

    async def listar_comentarios(self, imovel_id: int) -> List[Comentario]:
        imovel = self.__db_session.query(Imovel).filter(Imovel.id == imovel_id).first()
        if not imovel:
            raise HttpNotFoundError("Imóvel não encontrado.")
        
        comentarios = self.__db_session.query(Comentario).filter(Comentario.imovel == imovel).all()        
        return comentarios


    async def visualizar_comentario(self, comentario_id: int) -> Comentario:
        comentario = self.__db_session.query(Comentario).filter(Comentario.id == comentario_id).first()
        if not comentario:
            raise HttpNotFoundError("Comentário não encontrado.")
        return comentario


    async def atualizar_comentario(self, comentario_info: dict) -> Comentario:
        try:
            comentario = self.__db_session.query(Comentario).filter(Comentario.id == comentario_info.get("id")).first()
            if not comentario:
                raise HttpNotFoundError("Comentário não encontrado.")

            comentario.texto = comentario_info.get("texto")
            comentario.aprovado = comentario_info.get("aprovado")

            self.__db_session.commit()
            return await self.visualizar_comentario(comentario.id)
        except Exception as exception:
            self.__db_session.rollback()
            raise exception


    async def deletar_comentario(self, comentario_id: int) -> Comentario:    
        try:
            comentario = self.__db_session.query(Comentario).filter(Comentario.id == comentario_id).first()
            if not comentario:
                raise HttpNotFoundError("Comentário não encontrado.")
            
            self.__db_session.delete(comentario)
            self.__db_session.commit()
            return comentario
        except Exception as exception:
            self.__db_session.rollback()
            raise exception
        