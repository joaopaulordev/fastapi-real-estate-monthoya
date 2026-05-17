from abc import ABC, abstractmethod

class TipoImovelAtualizarControllerInterface(ABC):

    @abstractmethod
    async def atualizar(self, tipo_imovel_data: dict) -> dict: pass