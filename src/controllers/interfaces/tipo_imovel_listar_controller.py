from abc import ABC, abstractmethod

class TipoImovelListarControllerInterface(ABC):

    @abstractmethod
    async def listar(self) -> dict: pass
