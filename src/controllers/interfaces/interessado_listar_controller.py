from abc import ABC, abstractmethod

class InteressadoListarControllerInterface(ABC):

    @abstractmethod
    async def listar(self, imovel_id: int) -> dict: pass
