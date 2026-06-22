from abc import ABC, abstractmethod

class ConfigWhatsappListarControllerInterface(ABC):

    @abstractmethod
    async def listar(self) -> dict: pass
