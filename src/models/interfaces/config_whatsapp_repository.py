from typing import List
from abc import ABC, abstractmethod
from src.models.entities.imovel import ConfigWhatsapp

class ConfigWhatsappRepositoryInterface(ABC):

    @abstractmethod
    async def listar_configWhatsapps(self) -> List[ConfigWhatsapp]: pass

    @abstractmethod
    async def inserir_configWhatsapp(self, configwhatsapp_info: dict) -> ConfigWhatsapp: pass

    @abstractmethod
    async def visualizar_configWhatsapp(self, configwhatsapp_id: int) -> ConfigWhatsapp: pass

    @abstractmethod
    async def atualizar_configWhatsapp(self, configwhatsapp_info: dict) -> ConfigWhatsapp: pass

    @abstractmethod
    async def deletar_configWhatsapp(self, configwhatsapp_id: int) -> ConfigWhatsapp: pass