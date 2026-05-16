from abc import ABC, abstractmethod

class InteressadoDeletarControllerInterface(ABC):

    @abstractmethod
    async def deletar(self, interessado_id: int) -> dict: pass