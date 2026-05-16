from abc import ABC, abstractmethod

class ComentarioListarControllerInterface(ABC):

    @abstractmethod
    async def listar(self, imovel_id: int) -> dict: pass
