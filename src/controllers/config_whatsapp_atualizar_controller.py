from src.models.interfaces.config_whatsapp_repository import ConfigWhatsappRepositoryInterface
from src.errors.types.http_bad_request_error import HttpBadRequestError
from .interfaces.config_whatsapp_atualizar_controller import ConfigWhatsappAtualizarControllerInterface
from src.models.entities.imovel import ConfigWhatsapp

class ConfigWhatsappAtualizarController(ConfigWhatsappAtualizarControllerInterface):
    def __init__(self, configwhatsapp_repository: ConfigWhatsappRepositoryInterface) -> None:
        self._configwhatsapp_repository = configwhatsapp_repository

    async def atualizar(self, configwhatsapp_data: dict) -> dict:       
        self._validate_configwhatsapp_data(configwhatsapp_data)
        configwhatsapp = await self.__atualizar_configwhatsapp(configwhatsapp_data)
        return self.__format__response(configwhatsapp)

    def _validate_configwhatsapp_data(self, configwhatsapp_data: dict) -> None:
        telefone = configwhatsapp_data["telefone"]
        if not telefone:
            raise HttpBadRequestError("Telefone da config whatsapp é obrigatório.")        
        

    async def __atualizar_configwhatsapp(self, configwhatsapp_data: dict) -> ConfigWhatsapp:
        return await self._configwhatsapp_repository.atualizar_configWhatsapp(configwhatsapp_data)

    def __format__response(self, configwhatsapp: ConfigWhatsapp) -> dict:
        formatted_configwhatsapp = { "id": configwhatsapp.id, "ativo": configwhatsapp.ativo, "mensagem": configwhatsapp.mensagem, "telefone": configwhatsapp.telefone }
        return {
            "type": "ConfigWhatsapp",
            "count": 1,
            "config_whatsapp": formatted_configwhatsapp
        }