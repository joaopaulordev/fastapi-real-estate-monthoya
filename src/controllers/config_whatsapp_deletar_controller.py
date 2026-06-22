from src.models.interfaces.config_whatsapp_repository import ConfigWhatsappRepositoryInterface
from .interfaces.config_whatsapp_deletar_controller import ConfigWhatsappDeletarControllerInterface


class ConfigWhatsappDeletarController(ConfigWhatsappDeletarControllerInterface):
    def __init__(self, configwhatsapp_repository: ConfigWhatsappRepositoryInterface) -> None:
        self.__configwhatsapp_repository = configwhatsapp_repository

    async def deletar(self, configwhatsapp_id: int) -> dict:       
        configwhatsapp = await self.__configwhatsapp_repository.deletar_configWhatsapp(configwhatsapp_id)
        return {
            "message": f"Config Whatsapp {configwhatsapp.telefone} deletada com sucesso."
        }


