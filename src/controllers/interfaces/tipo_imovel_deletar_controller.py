from abc import ABC, abstractmethod

class TipoImovelDeletarControllerInterface(ABC):

    @abstractmethod
    async def deletar(self, tipo_imovel_id: int) -> dict: pass