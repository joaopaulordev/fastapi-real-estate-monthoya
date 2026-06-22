from abc import ABC, abstractmethod

class ConfigWhatsappDeletarControllerInterface(ABC):

    @abstractmethod
    async def deletar(self, configwhatsapp_id: int) -> dict: pass