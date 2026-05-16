from typing import List
from sqlalchemy.orm import Session
from src.errors.types.http_not_found_error import HttpNotFoundError
from src.models.interfaces.foto_repository import FotoRepositoryInterface
from src.models.entities.imovel import Foto, Imovel

class FotoRepository(FotoRepositoryInterface):
    def __init__(self, db: Session) -> None:
        self.__db_session = db


    async def listar_fotos(self, imovel_id: int) -> List[Foto]:
        imovel = self.__db_session.query(Imovel).filter(Imovel.id == imovel_id).first()
        if not imovel:
            raise HttpNotFoundError("Imóvel não encontrado.")
        
        fotos = self.__db_session.query(Foto).filter(Foto.imovel == imovel).all()        
        return fotos


    async def inserir_foto(self, foto_info: dict) -> None:
        try:
            imovel = self.__db_session.query(Imovel).filter(Imovel.id == foto_info["imovel_id"]).first()
            if not imovel:
                raise HttpNotFoundError("Imóvel não encontrado.")
            
            foto = self.__db_session.query(Foto).filter(Foto.caminho == foto_info["caminho"]).first()
            if not foto:
                foto = Foto(imovel=imovel, caminho=foto_info["caminho"])
                self.__db_session.add(foto)
                self.__db_session.commit()                        
        except Exception as exception:
            self.__db_session.rollback()
            raise exception
        

    async def deletar_foto(self, foto_id: int) -> Foto:
        try:
            foto = self.__db_session.query(Foto).filter(Foto.id == foto_id).first()
            if not foto:
                raise HttpNotFoundError("Foto não encontrada.")
            
            self.__db_session.delete(foto)
            self.__db_session.commit()
            return foto
        except Exception as exception:
            self.__db_session.rollback()
            raise exception
        