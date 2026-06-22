from src.models.interfaces.config_whatsapp_repository import ConfigWhatsappRepositoryInterface
from .interfaces.config_whatsapp_inserir_controller import ConfigWhatsappInserirControllerInterface
from src.errors.types.http_bad_request_error import HttpBadRequestError
from src.models.entities.imovel import ConfigWhatsapp

class ConfigWhatsappInserirController(ConfigWhatsappInserirControllerInterface):
    def __init__(self, configwhatsapp_repository: ConfigWhatsappRepositoryInterface) -> None:
        self._configwhatsapp_repository = configwhatsapp_repository

    async def inserir(self, configwhatsapp_data: dict) -> dict:        
        self._validate_configwhatsapp_data(configwhatsapp_data)
        configwhatsapp = await self.__inserir_configwhatsapp(configwhatsapp_data)
        return self.__format__response(configwhatsapp)
    

    def _validate_configwhatsapp_data(self, configwhatsapp_data: dict) -> None:
        if not configwhatsapp_data.get("telefone"):
            raise HttpBadRequestError("Telefone da config whatsapp é obrigatório.")
        
    
    async def __inserir_configwhatsapp(self, configwhatsapp_data: dict) -> ConfigWhatsapp:
        configwhatsapp = await self._configwhatsapp_repository.inserir_configWhatsapp(configwhatsapp_data)
        return configwhatsapp


    def __format__response(self, configwhatsapp: ConfigWhatsapp) -> dict:
        formatted_configwhatsapp = { "id": configwhatsapp.id, "ativo": configwhatsapp.ativo, "mensagem": configwhatsapp.mensagem, "telefone": configwhatsapp.telefone }
        return {
            "type": "ConfigWhatsapp",
            "count": 1,
            "config_whatsapp": formatted_configwhatsapp
        }