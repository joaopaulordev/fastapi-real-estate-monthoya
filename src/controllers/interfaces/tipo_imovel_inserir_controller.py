from abc import ABC, abstractmethod

class TipoImovelInserirControllerInterface(ABC):

    @abstractmethod
    async def inserir(self, tipo_imovel_data: dict) -> dict: pass