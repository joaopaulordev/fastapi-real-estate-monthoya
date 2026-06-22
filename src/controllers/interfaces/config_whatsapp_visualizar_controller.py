from abc import ABC, abstractmethod

class ConfigWhatsappVisualizarControllerInterface(ABC):

    @abstractmethod
    async def visualizar(self, configwhatsapp_id: int) -> dict: pass