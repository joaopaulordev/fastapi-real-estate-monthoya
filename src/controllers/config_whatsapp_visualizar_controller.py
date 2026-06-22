from src.models.interfaces.config_whatsapp_repository import ConfigWhatsappRepositoryInterface
from src.models.entities.imovel import ConfigWhatsapp
from .interfaces.config_whatsapp_visualizar_controller import ConfigWhatsappVisualizarControllerInterface

class ConfigWhatsappVisualizarController(ConfigWhatsappVisualizarControllerInterface):
    def __init__(self, configwhatsapp_repository: ConfigWhatsappRepositoryInterface) -> None:
        self.__configwhatsapp_repository = configwhatsapp_repository

    async def visualizar(self, configwhatsapp_id: int) -> dict:        
        configwhatsapp = await self.__busca_configwhatsapp_db(configwhatsapp_id)
        response = self.__format_response(configwhatsapp)
        return response

    async def __busca_configwhatsapp_db(self, configwhatsapp_id: int) -> ConfigWhatsapp:
        configwhatsapp = await self.__configwhatsapp_repository.visualizar_configWhatsapp(configwhatsapp_id)
        return configwhatsapp

    def __format_response(self, configwhatsapp: ConfigWhatsapp) -> dict:
        formatted_configwhatsapp = { "id": configwhatsapp.id, "ativo": configwhatsapp.ativo, "mensagem": configwhatsapp.mensagem, "telefone": configwhatsapp.telefone }
        return {            
            "type": "ConfigWhatsapp",
            "count": 1,
            "config_whatsapp": formatted_configwhatsapp        
        }