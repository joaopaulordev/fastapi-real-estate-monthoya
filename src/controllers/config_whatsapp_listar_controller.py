from typing import List
from src.models.interfaces.config_whatsapp_repository import ConfigWhatsappRepositoryInterface
from src.models.entities.imovel import ConfigWhatsapp
from .interfaces.config_whatsapp_listar_controller import ConfigWhatsappListarControllerInterface

class ConfigWhatsappListarController(ConfigWhatsappListarControllerInterface):
    def __init__(self, configwhatsapp_repository: ConfigWhatsappRepositoryInterface) -> None:
        self.__configwhatsapp_repository = configwhatsapp_repository

    async def listar(self) -> dict:        
        configwhatsapps = await self.__buscar_configwhatsapps_db()
        response = self.__format_response(configwhatsapps)
        return response

    async def __buscar_configwhatsapps_db(self) -> List[ConfigWhatsapp]:
        configwhatsapps = await self.__configwhatsapp_repository.listar_configWhatsapps()
        return configwhatsapps

    def __format_response(self, configwhatsapps: List[ConfigWhatsapp]) -> dict:
        formatted_configwhatsapps = [{ "id": configwhatsapp.id, "ativo": configwhatsapp.ativo, "mensagem": configwhatsapp.mensagem, "telefone": configwhatsapp.telefone} for configwhatsapp in configwhatsapps]
        return {
            "type": "ConfigWhatsapps",
            "count": len(formatted_configwhatsapps),
            "config_whatsapps": formatted_configwhatsapps            
        }
