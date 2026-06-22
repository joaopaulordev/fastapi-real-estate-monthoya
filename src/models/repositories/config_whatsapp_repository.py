from typing import List
from sqlalchemy.orm import Session
from src.errors.types.http_not_found_error import HttpNotFoundError
from src.models.interfaces.config_whatsapp_repository import ConfigWhatsappRepositoryInterface
from src.models.entities.imovel import ConfigWhatsapp

class ConfigWhatsappRepository(ConfigWhatsappRepositoryInterface):
    def __init__(self, db: Session) -> None:
        self.__db_session = db


    async def inserir_configWhatsapp(self, configwhatsapp_info: dict) -> ConfigWhatsapp:
        try:            
            configwhatsapp = ConfigWhatsapp(ativo=configwhatsapp_info.get("ativo"), mensagem=configwhatsapp_info.get("mensagem"), telefone=configwhatsapp_info.get("telefone"))
            self.__db_session.add(configwhatsapp)
            self.__db_session.commit()  
            return configwhatsapp                      
        except Exception as exception:
            self.__db_session.rollback()
            raise exception
        

    async def listar_configWhatsapps(self) -> List[ConfigWhatsapp]:
        return self.__db_session.query(ConfigWhatsapp).all()        


    async def visualizar_configWhatsapp(self, configwhatsapp_id: int) -> ConfigWhatsapp:
        configwhatsapp = self.__db_session.query(ConfigWhatsapp).filter(ConfigWhatsapp.id == configwhatsapp_id).first()
        if not configwhatsapp:
            raise HttpNotFoundError("ConfigWhatsapp não encontrada.")
        return configwhatsapp


    async def atualizar_configWhatsapp(self, configwhatsapp_info: dict) -> ConfigWhatsapp:
        try:
            configwhatsapp = self.__db_session.query(ConfigWhatsapp).filter(ConfigWhatsapp.id == configwhatsapp_info.get("id")).first()
            if not configwhatsapp:
                raise HttpNotFoundError("ConfigWhatsapp não encontrada.")

            configwhatsapp.ativo = configwhatsapp_info.get("ativo")            
            configwhatsapp.mensagem = configwhatsapp_info.get("mensagem")            
            configwhatsapp.telefone = configwhatsapp_info.get("telefone")            
            self.__db_session.commit()
            
            return configwhatsapp
        except Exception as exception:
            self.__db_session.rollback()
            raise exception


    async def deletar_configWhatsapp(self, configwhatsapp_id: int) -> ConfigWhatsapp:    
        try:
            configwhatsapp = self.__db_session.query(ConfigWhatsapp).filter(ConfigWhatsapp.id == configwhatsapp_id).first()
            if not configwhatsapp:
                raise HttpNotFoundError("ConfigWhatsapp não encontrada.")
            
            self.__db_session.delete(configwhatsapp)
            self.__db_session.commit()
            return configwhatsapp
        except Exception as exception:
            self.__db_session.rollback()
            raise exception
        