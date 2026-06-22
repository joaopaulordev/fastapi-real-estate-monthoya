from abc import ABC, abstractmethod

class ConfigWhatsappAtualizarControllerInterface(ABC):

    @abstractmethod
    async def atualizar(self, configwhatsapp_data: dict) -> dict: pass