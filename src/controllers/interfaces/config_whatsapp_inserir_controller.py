from abc import ABC, abstractmethod

class ConfigWhatsappInserirControllerInterface(ABC):

    @abstractmethod
    async def inserir(self, configwhatsapp_data: dict) -> dict: pass