from abc import ABC, abstractmethod

class FinalidadeListarControllerInterface(ABC):

    @abstractmethod
    async def listar(self) -> dict: pass
