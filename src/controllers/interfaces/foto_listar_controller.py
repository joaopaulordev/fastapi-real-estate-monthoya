from abc import ABC, abstractmethod

class FotoListarControllerInterface(ABC):

    @abstractmethod
    async def listar(self, imovel_id: int) -> dict: pass
